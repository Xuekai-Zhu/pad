def solution():
    """Mark has kangaroos and goats. Kangaroos have two legs and goats have four legs. If he has 23 kangaroos and three times as many goats as kangaroos what is the total number of legs of all his animals?"""
    kangaroo_legs = 2
    goat_legs = 4
    kangaroo_count = 23
    goat_count = 3 * kangaroo_count
    total_legs = (kangaroo_legs * kangaroo_count) + (goat_legs * goat_count)
    result = total_legs
    return result

print(solution())