from django.contrib import admin

# Register your models here.
from .models import Player, BuddyPokemon, Currency, EquippedBadge, DailyBonus, PlayerAvatar

admin.site.register(Player)
admin.site.register(BuddyPokemon)
admin.site.register(Currency)
admin.site.register(EquippedBadge)
admin.site.register(DailyBonus)
admin.site.register(PlayerAvatar)