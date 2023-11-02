def solution():
    """Derrick measures the length of his yard. The length of Alex's yard is half the size of Derrick's and the length of Brianne's yard is 6 times the size of Alex's. If Brianne's yard is 30 yards long, how long is Derrick's yard, in yards?"""
    # Define the length of Brianne's yard
    brianne_length = 30

    # Calculate the length of Alex's yard
    alex_length = brianne_length / 6

    # Calculate the length of Derrick's yard
    derrick_length = alex_length * 2

    # Display the length of Derrick's yard
    result = derrick_length
    return result

print(solution())