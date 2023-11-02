def solution():
    """Jake is from a conservative household so during lunch at school one day, he gave one-quarter of his feeding allowance to a hungry friend. If candies cost 20 cents apiece and Jake's feeding allowance is $4, how many candies can his friend purchase with the money Jake gave to him?"""
    # Define the feeding allowance
    feeding_allowance = 4

    # Calculate the amount of money Jake gave to his friend
    friend_allowance = feeding_allowance / 4

    # Calculate the number of candies that can be purchased with the friend's allowance
    candies = friend_allowance / 0.2

    # return the result
    result = int(candies)
    return result

print(solution())