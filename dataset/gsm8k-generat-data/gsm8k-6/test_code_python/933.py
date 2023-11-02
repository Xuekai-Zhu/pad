def solution():
    # Calculate the number of steps in each staircase
    staircase_one = 20
    staircase_two = 2 * staircase_one
    staircase_three = staircase_two - 10

    # Calculate the total number of steps John climbed
    total_steps = staircase_one + staircase_two + staircase_three

    # Calculate the total distance John climbed in feet
    distance_climbed = total_steps * 0.5

    result = distance_climbed
    return result

print(solution())