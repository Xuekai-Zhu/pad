def solution():
    """Fred had 212 sheets of paper. He received another 307 sheets of paper from Jane and gave Charles 156 sheets of paper. How many sheets of paper does Fred have left?"""
    # Define the initial number of sheets
    initial_sheets = 212

    # Define the number of sheets received from Jane
    jane_sheets = 307

    # Define the number of sheets given to Charles
    charles_sheets = 156

    # Calculate the total number of sheets after the transaction
    total_sheets = initial_sheets + jane_sheets - charles_sheets

    # Return the number of sheets Fred has left
    result = total_sheets
    return result

print(solution())