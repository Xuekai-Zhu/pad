def solution():
    num_sisters = 3
    start_clothes = 10

    # Calculate the number of clothes the first sister has
    sister1_clothes = start_clothes / 2

    # Calculate the number of clothes the second sister has
    sister2_clothes = start_clothes + 2

    # Calculate the total number of clothes all four sisters have
    total_clothes = start_clothes + sister1_clothes + sister2_clothes

    # Calculate the average number of clothes per sister
    avg_clothes = total_clothes / (num_sisters + 1)

    # Calculate the number of clothes Nicole ends up with
    nicole_clothes = avg_clothes

    result = nicole_clothes
    return result

print(solution())