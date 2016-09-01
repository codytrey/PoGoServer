from __future__ import unicode_literals

import time

from django.db import models

current_milli_time = lambda: int(round(time.time() * 1000))

# Create your models here.
class Player(models.Model):
    creation_timestamp_ms = models.BigIntegerField(db_column='creation_timestamp_ms', default=current_milli_time())
    username = models.CharField(max_length=40)
    team = models.IntegerField(db_column='team')
    tutorial_state = models.IntegerField(db_column='tutorial_state')
    max_pokemon_storage = models.IntegerField(db_column='max_pokemon_storage')
    max_item_storage = models.IntegerField(db_column='max_item_storage')
    remaining_codename_claims = models.IntegerField(db_column='remaining_codename_claims')


class BuddyPokemon(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    pokemon_id = models.BigIntegerField(db_column='pokemon_id',null=True)
    start_km_walked = models.FloatField(db_column='start_km_walked',null=True)
    last_km_awarded = models.FloatField(db_column='last_km_awarded',null=True)


class Currency(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(db_column='name',max_length=40,null=True)
    amount = models.IntegerField(db_column='amount',null=True)


class EquippedBadge(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.IntegerField(db_column='level',null=True)
    next_equip_change_allowed_timestamp_ms = models.BigIntegerField(db_column='next_equip_change_allowed_timestamp_ms',null=True)
    equipped_badge = models.TextField(db_column='equipped_badge',null=True)


class DailyBonus(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    next_collected_timestamp_ms = models.BigIntegerField(db_column='next_collected_timestamp_ms',null=True)
    next_defender_bonus_collect_timestamp_ms = models.BigIntegerField(db_column='next_defender_bonus_collect_timestamp_ms',null=True)


class PlayerAvatar(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    skin = models.IntegerField(db_column='skin',null=True)
    hair = models.IntegerField(db_column='hair',null=True)
    shirt = models.IntegerField(db_column='shirt',null=True)
    pants = models.IntegerField(db_column='pants',null=True)
    hat = models.IntegerField(db_column='hat',null=True)
    shoes = models.IntegerField(db_column='shoes',null=True)
    eyes = models.IntegerField(db_column='eyes',null=True)
    backpack = models.IntegerField(db_column='backpack',null=True)
    gender = models.BinaryField(db_column='gender',null=True)
