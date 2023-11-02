def solution():
    """Max loves to play video games. He played for 2 hours on Wednesday and the same time on Thursday. On Friday his friends came to play together with him, so Max spent over three hours more on playing than on Wednesday. How many hours on average has Max spent playing video games during these three days?"""
    wednesday_hours = 2
    thursday_hours = 2
    friday_hours = wednesday_hours + 3

    total_hours = wednesday_hours + thursday_hours + friday_hours
    average_hours = total_hours / 3
    result = average_hours
    return result

print(solution())