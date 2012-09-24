from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    # This field is required
    user = models.OneToOneField(User)

    # Other fields here
    onefiftyK = '150K'
    BUSINESS_DEVELOPMENT = 'BIZDEV'
    EBOOTCAMP = 'EBC'
    FORGE = 'FGE'
    FRESHMAN_BATTALION = 'FBA'
    TECH_TEAM = 'TECH'
    UNASSIGNED = 'UNA'
    
    TEAM_CHOICES = (
        (onefiftyK, '150K Challenge'),
        (BUSINESS_DEVELOPMENT, 'Business Development'),
        (EBOOTCAMP, 'E-Bootcamp'),
        (FORGE, 'Forge'),
        (FRESHMAN_BATTALION, 'Freshman Battalion'),
        (TECH_TEAM, 'Tech Team'),
        (UNASSIGNED, 'Unassigned'),
    )
    team = models.CharField(max_length=10,
                            choices=TEAM_CHOICES,
                            default=UNASSIGNED)
    def is_vp(self):
        return self.user.groups.filter(name="VP").exists()

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
