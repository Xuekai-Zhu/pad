def solution():
    """Ginger and Amy both start with 100 pieces of Halloween candy. Ginger eats 4 pieces a day and Amy eats 3 pieces a day. How much more candy does Amy have after two weeks?"""
    starting_candy = 100
    ginger_eats_per_day = 4
    amy_eats_per_day = 3
    days = 14
    ginger_candy_left = starting_candy - (ginger_eats_per_day * days)
    amy_candy_left = starting_candy - (amy_eats_per_day * days)
    difference = amy_candy_left - ginger_candy_left
    result = difference
    return result

print(solution())