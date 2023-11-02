def solution():
    """With one mighty blow, Maria cracked open the pinata, and candies spilled all over the floor.  There were 40 red candies, 20 less than three times as many yellow candies as red candies, and half as many blue candies as yellow candies.  If Carlos ate all of the yellow candies, how many candies remained?"""
    # Define the initial number of red candies
    red_candies = 40

    # Calculate the number of yellow candies
    yellow_candies = (red_candies * 3) - 20

    # Calculate the number of blue candies
    blue_candies = yellow_candies / 2

    # Calculate the total number of candies
    total_candies = red_candies + yellow_candies + blue_candies

    # Calculate the number of candies remaining after Carlos eats all of the yellow candies
    candies_remaining = total_candies - yellow_candies

    # return the result
    result = candies_remaining
    return result

print(solution())