def solution():
    # Define the ratio of the number of fish Alex caught to the number Jacob caught
    alex_to_jacob_ratio = 7

    # Calculate the number of fish Alex initially caught
    initial_alex_fish = jacob_fish * alex_to_jacob_ratio

    # Calculate the number of fish Alex caught after losing 23
    final_alex_fish = initial_alex_fish - 23

    # Calculate the number of fish Jacob needs to catch to beat Alex by 1 fish
    one_fish_difference = final_alex_fish - jacob_fish + 1
    result = one_fish_difference
    return result

print(solution())