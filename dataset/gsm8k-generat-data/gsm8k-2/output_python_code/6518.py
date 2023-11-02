def solution():
    """A snail kite is a kind of bird that eats apple snails. On the first day, a snail kite ate 3 snails. Then it eats 2 more snails than it did the day before. How many apple snails in all did a snail kite eat for 5 days?"""
    snails_on_first_day = 3
    snails_on_previous_day = snails_on_first_day
    total_snails = snails_on_first_day
    for i in range(1, 5):
        snails_on_current_day = snails_on_previous_day + 2
        total_snails += snails_on_current_day
        snails_on_previous_day = snails_on_current_day

    result = total_snails
    return result

print(solution())