def solution():
    """Andy had a platter of chocolate cookies. He ate 3 of them then gave his little brother 5 because he was behaving. He then handed the platter to his basketball team of eight members. The first player to arrive took 1, the second player to arrive took 3, the third player took 5, and so on. When the last player took his share, the platter was empty. How many chocolate cookies did Andy have from start with?"""
    # Define the number of cookies Andy started with
    initial_cookies = 0

    # Calculate the number of cookies Andy had after eating 3 and giving 5 to his brother
    initial_cookies += (3 - 5)

    # Calculate the total number of cookies taken by the basketball team
    total_cookies_taken = 0
    for i in range(1, 9):
        total_cookies_taken += 2 * i - 1

    # Calculate the number of cookies Andy started with
    final_cookies = initial_cookies + total_cookies_taken

    # Display the number of cookies Andy started with
    result = final_cookies
    return result

print(solution())