def solution():
    # Define the starting number of clothes
    starting_clothes = 10

    # Calculate the number of clothes Nicole's first sister had
    sister1_clothes = starting_clothes / 2

    # Calculate the number of clothes Nicole's second sister had
    sister2_clothes = starting_clothes + 2

    # Calculate the total number of clothes before the oldest sister gave hers
    total_clothes_before = starting_clothes + sister1_clothes + sister2_clothes

    # Calculate the average number of clothes among the three younger sisters
    avg_clothes_younger_sisters = total_clothes_before / 3

    # Calculate the number of clothes the oldest sister had
    sister3_clothes = avg_clothes_younger_sisters

    # Calculate the total number of clothes Nicole ends up with
    total_clothes_after = total_clothes_before + sister3_clothes

    result = total_clothes_after
    return result

print(solution())