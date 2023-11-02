def solution():
    """There are 9,300 pennies in a cup. What is the total dollar amount in a stack that contains two thirds of the pennies in the cup?"""
    pennies_in_cup = 9300
    fraction_of_pennies = 2/3
    pennies_in_stack = pennies_in_cup * fraction_of_pennies
    dollars_in_stack = pennies_in_stack / 100
    result = dollars_in_stack
    return result

print(solution())