def solution():
    """Bert made 12 sandwiches for his trip. On the first day, he ate half of the sandwiches he made. The next day he ate 2 sandwiches less. How many sandwiches does Bert have left after these two days?"""
    sandwiches_made = 12
    sandwiches_first_day = sandwiches_made / 2
    sandwiches_second_day = sandwiches_first_day - 2
    sandwiches_left = sandwiches_made - sandwiches_first_day - sandwiches_second_day
    result = sandwiches_left
    
    return result

print(solution())