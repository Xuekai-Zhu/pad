def solution():
    """Max loves to play video games. He played for 2 hours on Wednesday and the same time on Thursday. On Friday his friends came to play together with him, so Max spent over three hours more on playing than on Wednesday. How many hours on average has Max spent playing video games during these three days?"""
    wed_hours = 2
    thurs_hours = 2
    fri_hours = wed_hours + 3 + thurs_hours + 3
    total_hours = wed_hours + thurs_hours + fri_hours
    avg_hours = total_hours / 3
    result = avg_hours
    return result

print(solution())