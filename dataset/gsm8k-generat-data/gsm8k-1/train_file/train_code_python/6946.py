def solution():
    """In the garden, the gecko eats 12 bugs. The lizard eats half as many bugs as the gecko. The frog eats 3 times as many bugs as the lizard. The toad eats 50% more bugs than the frog. How many bugs are eaten in total by all of them?"""
    gecko = 12
    lizard = gecko / 2
    frog = lizard * 3
    toad = frog * 1.5
    total_bugs = gecko + lizard + frog + toad
    result = total_bugs
    return result

print(solution())