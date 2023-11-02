def solution():
    brian_fishing_freq = 2
    brian_fish_per_trip = 0.6  # 2/5 times fewer than Chris
    brian_fish_per_day = 400

    chris_fishing_freq = 1
    chris_fishing_days = 10

    # Calculate the total number of fish caught by Brian
    total_brian_fish = brian_fish_per_day * brian_fishing_days * brian_fishing_freq

    # Calculate the total number of fish caught by Chris
    total_chris_fish = total_brian_fish / (1 - brian_fish_per_trip)

    # Calculate the total number of fish caught by both of them
    total_fish = total_brian_fish + total_chris_fish
    result = total_fish
    return result

print(solution())