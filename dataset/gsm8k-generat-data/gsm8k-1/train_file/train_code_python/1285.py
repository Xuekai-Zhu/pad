def solution():
    """Olga has an aquarium with fish in 5 different colors. There are 12 yellow ones, half as many blue ones, and twice as many green ones as yellow ones. How many fish does Olga have in her aquarium?"""
    yellow_fish = 12
    blue_fish = yellow_fish / 2
    green_fish = yellow_fish * 2
    total_fish = yellow_fish + blue_fish + green_fish
    result = total_fish
    return result

print(solution())