def solution():
    """Mr. Sam shared a certain amount of money between his two sons, Ken and Tony. If Ken got $1750, and Tony got twice as much as Ken, how much was the money shared?"""
    # Define the amount of money that Ken received
    ken_money = 1750

    # Calculate the amount of money that Tony received
    tony_money = ken_money * 2

    # Calculate the total amount of money shared
    total_money = ken_money + tony_money

    # return the result
    result = total_money
    return result

print(solution())