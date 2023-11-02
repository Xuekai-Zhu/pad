def solution():
    """Bob enters cycling competitions every single week and hopes to win the 100 dollar grand prize each time. For the first 2 weeks, he managed first place and got 100 dollars each week. He is saving up for a puppy that costs 1000 dollars. What is the minimum number of additional weeks Bob must win first place?"""
    # Define the initial amount of money Bob has
    initial_money = 200

    # Define the cost of the puppy
    puppy_cost = 1000

    # Calculate the amount of money Bob needs to save up
    money_needed = puppy_cost - initial_money

    # Calculate the minimum number of additional weeks Bob must win first place
    additional_weeks = money_needed / 100

    # Round up the number of additional weeks to ensure Bob has enough money for the puppy
    additional_weeks = math.ceil(additional_weeks)

    # Display the minimum number of additional weeks Bob must win first place
    result = additional_weeks
    return result

print(solution())