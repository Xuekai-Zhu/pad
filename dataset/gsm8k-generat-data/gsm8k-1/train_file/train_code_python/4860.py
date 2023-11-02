def solution():
    """Amalia can read 4 pages of her book in 2 minutes. How many minutes will it take her to read 18 pages of her book?"""
    pages_per_time = 4/2 #pages/min
    pages_needed = 18
    minutes_needed = pages_needed/pages_per_time
    result = minutes_needed
    return result

print(solution())