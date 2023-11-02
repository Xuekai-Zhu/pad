def solution():
    """Derrick measures the length of his yard. The length of Alex's yard is half the size of Derrick's and the length of Brianne's yard is 6 times the size of Alex's. If Brianne's yard is 30 yards long, how long is Derrick's yard, in yards?"""
    # Define the length of Brianne's yard
    briannes_yard = 30

    # Calculate the length of Alex's yard
    alexs_yard = briannes_yard / 6

    # Calculate the length of Derrick's yard
    derricks_yard = alexs_yard * 2

    # return the result
    result = derricks_yard
    return result

print(solution())