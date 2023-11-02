def solution():
    """A dog barks 30 times per minute. If 2 dogs bark 30 times per minute, how many times will they have barked after 10 minutes?"""
    barks_per_minute = 30
    total_dogs = 2
    total_time = 10
    total_barks = barks_per_minute * total_dogs * total_time
    result = total_barks
    return result

print(solution())