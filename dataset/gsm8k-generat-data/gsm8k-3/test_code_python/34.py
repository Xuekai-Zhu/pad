def solution():
    """Mr. Sam shared a certain amount of money between his two sons, Ken and Tony. If Ken got $1750, and Tony got twice as much as Ken, how much was the money shared?"""
    # Define the amount Ken received
    ken_share = 1750

    # Calculate the amount Tony received
    tony_share = ken_share * 2

    # Calculate the total amount shared
    total_share = ken_share + tony_share

    # return the result
    result = total_share
    return result

print(solution())