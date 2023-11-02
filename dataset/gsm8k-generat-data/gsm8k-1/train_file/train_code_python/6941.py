def solution():
    """Mark has kangaroos and goats. Kangaroos have two legs and goats have four legs. If he has 23 kangaroos and three times as many goats as kangaroos what is the total number of legs of all his animals?"""
    kangaroo_legs = 2
    goat_legs = 4
    num_kangaroos = 23
    num_goats = num_kangaroos * 3
    total_legs = (num_kangaroos * kangaroo_legs) + (num_goats * goat_legs)
    result = total_legs
    return result

print(solution())