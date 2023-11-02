def solution():
    """Alyssa and Abigail need to collect 100 empty cans for their Science project. As of today, Alyssa collected 30 while Abigail collected 43 empty cans. How many more empty cans should they collect?"""
    # Define the number of cans collected by Alyssa and Abigail
    alyssa_cans = 30
    abigail_cans = 43

    # Calculate the total number of cans needed
    total_cans = 100

    # Calculate the number of cans left to collect
    cans_left = total_cans - alyssa_cans - abigail_cans

    # Display the number of cans left to collect
    result = cans_left
    return result

print(solution())