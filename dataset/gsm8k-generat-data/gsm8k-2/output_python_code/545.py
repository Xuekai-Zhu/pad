def solution():
    """John received 20 gifts on his 12th birthday. He received 8 fewer gifts on his 13th birthday. How many total gifts did he receive between those two birthdays?"""
    gifts_on_12th_birthday = 20
    gifts_on_13th_birthday = gifts_on_12th_birthday - 8
    total_gifts = gifts_on_12th_birthday + gifts_on_13th_birthday
    result = total_gifts
    return result

print(solution())