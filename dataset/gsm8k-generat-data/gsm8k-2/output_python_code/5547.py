def solution():
    """Kira's cat eats a pound of kibble every 4 hours. Kira fills her cat's bowl with 3 pounds of kibble before going to work. When she returns, Kira weighs the bowl and there is still 1 pound left. How many hours was Kira away from home?"""
    cat_eats_per_hour = 0.25   # 1 pound every 4 hours
    initial_kibble = 3
    remaining_kibble = 1
    hours_away = ((initial_kibble - remaining_kibble) / cat_eats_per_hour)
    result = hours_away
    return result

print(solution())