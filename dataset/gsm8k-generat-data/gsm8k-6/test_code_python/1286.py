def solution():
    # Calculate the total number of fish in Olga's aquarium
    yellow_fish = 12
    blue_fish = yellow_fish / 2
    green_fish = yellow_fish * 2
    total_fish = yellow_fish + blue_fish + green_fish + (5 + 7 + 9)  # assuming there are 5 red fish, 7 orange fish, and 9 purple fish in the aquarium
    result = total_fish
    return result

print(solution())