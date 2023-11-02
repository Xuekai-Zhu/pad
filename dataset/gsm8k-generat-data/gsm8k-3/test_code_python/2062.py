def solution():
    """Joan has 2 hours to get all her music practice done. She spends 30 minutes on the piano, 25 minutes writing music on her computer, and 38 minutes reading about the history of the piano. Her final work is to use a special finger exerciser. How much time does she have left to use this?"""
    # Define the total time Joan has to practice
    total_time = 2 * 60 # in minutes

    # Subtract the time spent on the piano, writing music, and reading about piano history
    remaining_time = total_time - 30 - 25 - 38

    # Display the remaining time
    result = remaining_time
    return result

print(solution())