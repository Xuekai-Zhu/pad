def solution():
    """Jenny wants to read 3 books in the next 10 days. She can read 100 words per hour. If the first book has 200 words, the second book has 400 words, and the third book has 300 words, how many minutes per day, on average, should she spend reading?"""
    total_words = 200 + 400 + 300
    total_hours = total_words / 100
    days = 10
    minutes_per_day = total_hours / days * 60
    result = minutes_per_day
    return result

print(solution())