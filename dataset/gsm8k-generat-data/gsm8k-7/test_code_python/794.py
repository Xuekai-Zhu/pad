def solution():
    num_red_candies = 40
    num_yellow_candies = 3 * num_red_candies - 20
    num_blue_candies = num_yellow_candies / 2

    # Calculate the total number of candies
    total_candies = num_red_candies + num_yellow_candies + num_blue_candies

    # Carlos eats all yellow candies
    num_remaining_candies = total_candies - num_yellow_candies
    result = num_remaining_candies
    return result

print(solution())