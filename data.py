def getMedals(toParse, hero, mode):
    #Get data and return
    medals = [toParse['eu']['heroes']['stats'][mode][hero]['general_stats']['medals'],
              toParse['eu']['heroes']['stats'][mode][hero]['general_stats']['medals_bronze'],
              toParse['eu']['heroes']['stats'][mode][hero]['general_stats']['medals_silver'],
              toParse['eu']['heroes']['stats'][mode][hero]['general_stats']['medals_gold']]

    return medals

def getHeal(toParse, hero, mode):
    #Get data and return
    heal = toParse['eu']['heroes']['stats'][mode][hero]['general_stats']['healing_done']

    return heal

def getDamage(toParse, hero, mode):
    #Get data and return
    damage = toParse['eu']['heroes']['stats'][mode][hero]['average_stats']['damage_done_average']

    return damage

def getWeaponAccuracy(toParse, hero, mode):
    #Get data and return
    wa = toParse['eu']['heroes']['stats'][mode][hero]['general_stats']['weapon_accuracy']

    return wa

def getBlockedDamage(toParse, hero, mode):
    #Get data and return
    blocked = toParse['eu']['heroes']['stats'][mode][hero]['average_stats']['damage_blocked_average']

    return blocked

def getScopedAccuracy(toParse, hero, mode):
    #Get data and return
    scoped = toParse['eu']['heroes']['stats'][mode][hero]['hero_stats']['scoped_accuracy']

    return scoped

def getGeneralStats(toParse, hero, mode):
    #Get list of data and return
    prestige = toParse['eu']['stats'][mode]['overall_stats']['prestige']
    level = prestige * 100 + toParse['eu']['stats'][mode]['overall_stats']['level']
    win_rate = toParse['eu']['stats'][mode]['overall_stats']['win_rate']
    tier = toParse['eu']['stats'][mode]['overall_stats']['tier']
    elo = toParse['eu']['stats'][mode]['overall_stats']['comprank']
    player_time = toParse['eu']['stats'][mode]['game_stats']['time_played']
    hero_time = toParse['eu']['heroes']['playtime'][mode][hero]

    return [level, tier, elo, win_rate, player_time, hero_time]
