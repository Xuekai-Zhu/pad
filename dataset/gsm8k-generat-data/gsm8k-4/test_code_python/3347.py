def solution():
    """Barbara has 9 stuffed animals. Trish has two times as many stuffed animals as Barbara. They planned to sell their stuffed animals and donate all the money to their class funds. Barbara will sell her stuffed animals for $2 each while Trish will sell them for $1.50 each. How much money will they donate to their class funds?"""
    # Define the number of stuffed animals each person has
    barbara_animals = 9
    trish_animals = 2 * barbara_animals

    # Calculate the total amount of money Barbara will make
    barbara_money = barbara_animals * 2

    # Calculate the total amount of money Trish will make
    trish_money = trish_animals * 1.5

    # Calculate the total amount of money they will donate to their class funds
    total_money = barbara_money + trish_money

    result = total_money
    return result

print(solution())