def solution():
    """Lena played video games for 3.5 hours last weekend. Her brother played 17 minutes more than she did. How many minutes together did Lena and her brother play video games last weekend?"""
    lena_time = 3.5 * 60  # convert hours to minutes
    brother_time = lena_time + 17
    total_time = lena_time + brother_time
    result = total_time
    return result

print(solution())