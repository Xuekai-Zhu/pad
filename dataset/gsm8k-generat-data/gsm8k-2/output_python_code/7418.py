def solution():
    """Tapanga and Corey have 66 candies together. However, Tapanga has 8 more candies than Corey. How many candies does Corey have?"""
    total_candies = 66
    tapanga_candies = (total_candies + 8) / 2
    corey_candies = total_candies - tapanga_candies
    result = corey_candies
    return result

print(solution())