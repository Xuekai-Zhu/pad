def solution():
    """Tiffany is measuring how many surfers can ride a big wave without falling. She sees that when a wave over 30 feet arrives, only 25% of the riders can stay upright. Of these riders, 60% are women. If there are 100 riders, how many men can stay upright on the wave?"""
    total_riders = 100
    upright_percent = 0.25
    upright_riders = total_riders * upright_percent
    women_percent = 0.6
    women_upright = upright_riders * women_percent
    men_upright = upright_riders - women_upright
    result = men_upright
    return result

print(solution())