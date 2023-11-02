def solution():
    # Calculate the number of fish in the first tank
    fish_first_tank = 7 + 8  

    # Calculate the number of fish in the second tank
    fish_second_tank = 2 * fish_first_tank  

    # Calculate the number of fish in the third tank
    fish_third_tank = fish_second_tank // 3 

    result = fish_third_tank
    return result

print(solution())