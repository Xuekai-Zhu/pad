def solution():
    """John received 20 gifts on his 12th birthday.  He received 8 fewer gifts on his 13th birthday.  How many total gifts did he receive between those two birthdays?"""
    # Define the number of gifts received on John's 12th birthday
    gifts_12 = 20

    # Calculate the number of gifts received on John's 13th birthday
    gifts_13 = gifts_12 - 8

    # Calculate the total number of gifts received between the two birthdays
    total_gifts = gifts_12 + gifts_13

    # Display the total number of gifts received
    result = total_gifts
    return result

print(solution())