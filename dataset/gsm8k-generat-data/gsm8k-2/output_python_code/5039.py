def solution():
    """There are 320 ducks in a pond. On the first night 1/4 of them get eaten by a fox. On the second night 1/6 of the remaining ducks fly away, and on the third night 30 percent are stolen. How many ducks remain after the three nights?"""
    total_ducks = 320
    fox_eaten = total_ducks // 4
    remaining_ducks = total_ducks - fox_eaten
    flying_away = remaining_ducks // 6
    remaining_ducks -= flying_away
    stolen = int(remaining_ducks * 0.3)
    remaining_ducks -= stolen
    result = remaining_ducks
    return result

print(solution())