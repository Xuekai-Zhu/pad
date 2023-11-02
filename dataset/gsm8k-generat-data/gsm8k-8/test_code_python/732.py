def solution():
    # Calculate the number of baby tarantulas in 5 egg sacs
    num_tarantulas = 1000*5

    # Calculate the total number of legs in 5 egg sacs
    total_legs = num_tarantulas*8

    # Calculate the number of legs in one less than 5 egg sacs
    legs_in_less_1_sac = (num_tarantulas-1)*8

    result = legs_in_less_1_sac
    return result

print(solution())