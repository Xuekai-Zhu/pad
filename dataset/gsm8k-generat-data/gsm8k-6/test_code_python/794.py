def solution():
    # Calculate the total number of candies
    red_candies = 40
    yellow_candies = 3 * red_candies - 20
    blue_candies = yellow_candies / 2
    total_candies = red_candies + yellow_candies + blue_candies

    # Calculate the number of candies remaining after Carlos ate all the yellow candies
    candies_remaining = total_candies - yellow_candies
    result = candies_remaining
    return result

print(solution())