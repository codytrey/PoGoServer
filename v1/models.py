from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Player(models.Model):
    creation_timestamp_ms = models.BigIntegerField
    username = models.CharField(max_length=40)
    team = models.IntegerField
    tutorial_state = models.IntegerField
    max_pokemon_storage = models.IntegerField
    max_item_storage = models.IntegerField
    remaining_codename_claims = models.IntegerField

class EquippedBadge(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.IntegerField
    next_equip_change_allowed_timestamp_ms = models.BigIntegerField


class DailyBonus(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    next_collected_timestamp_ms = models.BigIntegerField
    next_defender_bonus_collect_timestamp_ms = models.BigIntegerField

class PlayerAvatar(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    skin = models.IntegerField
    hair  = models.IntegerField
    shirt  = models.IntegerField
    pants  = models.IntegerField
    hat  = models.IntegerField
    shoes = models.IntegerField
    eyes  = models.IntegerField
    backpack = models.IntegerField
    gender = models.BinaryField