def solution():
    """Lena played video games for 3.5 hours last weekend. Her brother played 17 minutes more than she did. How many minutes together did Lena and her brother play video games last weekend?"""
    lena_time_hours = 3.5
    lena_time_minutes = lena_time_hours * 60
    brother_time_minutes = lena_time_minutes + 17
    total_time_minutes = lena_time_minutes + brother_time_minutes
    result = total_time_minutes
    return result

print(solution())