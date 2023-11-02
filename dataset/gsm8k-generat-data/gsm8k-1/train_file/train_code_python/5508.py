def solution():
    """A box of rainbow nerds contains 10 purple candies, 4 more yellow candies, and 2 fewer green candies than yellow candies. How many rainbow nerds are there in the box?"""
    purple_candies = 10
    yellow_candies = purple_candies + 4
    green_candies = yellow_candies - 2
    total_candies = purple_candies + yellow_candies + green_candies
    result = total_candies
    return result

print(solution())