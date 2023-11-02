def solution():
    # Calculate the number of tennis balls Ralph did not hit
    first_set = 100 * (1 - 2/5)  # calculate the number of tennis balls Ralph did not hit in the first set of 100
    second_set = 75 * (2/3)  # calculate the number of tennis balls Ralph hit in the second set of 75
    total_not_hit = 175 - (first_set + second_set)  # calculate the total number of tennis balls Ralph did not hit
    result = total_not_hit
    return result

print(solution())