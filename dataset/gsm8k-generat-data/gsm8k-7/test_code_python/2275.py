def solution():
    num_apples_bought = 6

    # Calculate the number of apples that Mary planted
    num_apples_planted = num_apples_bought * 2

    # Calculate the number of apples that Mary didn't eat or plant
    num_apples_left = num_apples_bought - num_apples_planted

    # Calculate the number of apples that Mary ate
    num_apples_ate = num_apples_bought - num_apples_left
    result = num_apples_ate
    return result

print(solution())