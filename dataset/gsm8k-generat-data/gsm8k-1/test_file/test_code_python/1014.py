def solution():
    """It takes James 10 minutes to read 3 pages of his book before he goes to bed. He reads 18 pages of his book and then decides to go to sleep. How long does James spend reading, in minutes?"""
    pages_per_minute = 3/10
    pages_read = 18
    time_spent = pages_read / pages_per_minute
    result = time_spent
    return result

print(solution())