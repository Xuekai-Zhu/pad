def solution():
    """A large bag of Starbursts candy has 232 pieces of individually wrapped candies. If this bag has 54 red candies, twice that amount of orange candies and half as many yellow candies as red candies, how many candies are pink?"""
    total_candies = 232
    red_candies = 54
    orange_candies = 2 * red_candies
    yellow_candies = red_candies / 2
    pink_candies = total_candies - (red_candies + orange_candies + yellow_candies)
    result = pink_candies
    return result

print(solution())