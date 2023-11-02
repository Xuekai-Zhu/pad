def solution():
    """Nancy has a bag containing 22 tortilla chips. She gives 7 tortilla chips to her brother and 5 tortilla chips to her sister, keeping the rest for herself. How many did Nancy keep for herself?"""
    # Define the total number of tortilla chips
    total_chips = 22

    # Calculate the number of chips given to Nancy's brother and sister
    given_chips = 7 + 5

    # Calculate the number of chips Nancy kept for herself
    self_chips = total_chips - given_chips

    # Display the number of chips Nancy kept for herself
    result = self_chips
    return result

print(solution())