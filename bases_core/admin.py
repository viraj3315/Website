from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from bases_core.models import UserProfile

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):

    # don't let non-superusers modify superusers
    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        if not request.user.is_superuser:
            qs = qs.exclude(Q(is_superuser=True))
        return qs

    def user_change_password(self, request, id):
        if request.user.pk != int(id) and not request.user.is_superuser:
            raise PermissionDenied
        return super(UserAdmin, self).user_change_password(request, id)

    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
