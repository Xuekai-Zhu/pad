def solution():
    """Bob enters cycling competitions every single week and hopes to win the 100 dollar grand prize each time. For the first 2 weeks, he managed first place and got 100 dollars each week. He is saving up for a puppy that costs 1000 dollars. What is the minimum number of additional weeks Bob must win first place?"""
    # Define the amount of money Bob has saved so far
    saved_money = 200

    # Define the cost of the puppy
    puppy_cost = 1000

    # Calculate the number of additional weeks Bob needs to save up for the puppy
    additional_weeks = (puppy_cost - saved_money) / 100

    # Round up to the nearest whole number of weeks
    additional_weeks = math.ceil(additional_weeks)

    # Return the result
    result = additional_weeks
    return result

print(solution())