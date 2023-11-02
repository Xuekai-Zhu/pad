def solution():
    """With one mighty blow, Maria cracked open the pinata, and candies spilled all over the floor. There were 40 red candies, 20 less than three times as many yellow candies as red candies, and half as many blue candies as yellow candies. If Carlos ate all of the yellow candies, how many candies remained?"""
    red_candies = 40
    yellow_candies = (3*red_candies) - 20
    blue_candies = yellow_candies / 2
    total_candies = red_candies + yellow_candies + blue_candies
    remaining_candies = total_candies - yellow_candies
    result = remaining_candies
    return result

print(solution())