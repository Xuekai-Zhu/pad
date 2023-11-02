def solution():
    """In the garden, the gecko eats 12 bugs. The lizard eats half as many bugs as the gecko. The frog eats 3 times as many bugs as the lizard. The toad eats 50% more bugs than the frog. How many bugs are eaten in total by all of them?"""
    gecko_eats = 12
    lizard_eats = gecko_eats / 2
    frog_eats = 3 * lizard_eats
    toad_eats = 1.5 * frog_eats
    total_bugs_eaten = gecko_eats + lizard_eats + frog_eats + toad_eats
    result = total_bugs_eaten
    return result

print(solution())