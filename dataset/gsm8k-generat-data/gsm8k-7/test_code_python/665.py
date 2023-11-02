def solution():
    num_apples_picked = 50
    num_apples_given_to_each_child = 6  # 3 apples each for 2 kids
    num_apples_used_for_pie = 20  # 10 apples per pie

    # Calculate the total number of apples given away
    total_apples_given_away = num_apples_given_to_each_child * 2

    # Calculate the total number of apples used for pies
    total_apples_used_for_pies = num_apples_used_for_pie * 2

    # Calculate the total number of apples left
    total_apples_left = num_apples_picked - total_apples_given_away - total_apples_used_for_pies
    result = total_apples_left
    return result

print(solution())