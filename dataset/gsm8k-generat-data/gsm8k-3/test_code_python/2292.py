def solution():
    """Jake is from a conservative household so during lunch at school one day, he gave one-quarter of his feeding allowance to a hungry friend. If candies cost 20 cents apiece and Jake's feeding allowance is $4, how many candies can his friend purchase with the money Jake gave to him?"""
    # Define the total feeding allowance
    ALLOWANCE = 4

    # Calculate the amount of Jake's allowance he gave to his friend
    friend_allowance = ALLOWANCE * 0.25

    # Calculate the number of candies his friend can purchase
    candies = friend_allowance / 0.2

    # Display the number of candies his friend can purchase
    result = candies
    return result

print(solution())