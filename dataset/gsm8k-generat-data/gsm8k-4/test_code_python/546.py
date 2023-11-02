def solution():
    """John received 20 gifts on his 12th birthday. He received 8 fewer gifts on his 13th birthday. How many total gifts did he receive between those two birthdays?"""
    # Define the number of gifts received on his 12th birthday
    gifts_12th_bday = 20

    # Calculate the number of gifts received on his 13th birthday
    gifts_13th_bday = gifts_12th_bday - 8

    # Calculate the total number of gifts received between those two birthdays
    total_gifts = gifts_12th_bday + gifts_13th_bday

    result = total_gifts
    return result

print(solution())