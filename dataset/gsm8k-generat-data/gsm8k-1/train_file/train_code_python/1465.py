def solution():
    """A dog barks 30 times per minute. If 2 dogs bark 30 times per minute, how many times will they have barked after 10 minutes?"""
    barks_per_minute = 30
    number_of_dogs = 2
    minutes = 10
    total_barks = barks_per_minute * number_of_dogs * minutes
    result = total_barks
    return result

print(solution())