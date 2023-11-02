def solution():
    """Emily has 6 marbles. Megan gives Emily double the number she has. Emily then gives Megan back half of her new total plus 1. How many marbles does Emily have now?"""
    emily_marbles = 6
    megan_marbles = emily_marbles * 2
    emily_new_total = emily_marbles + megan_marbles
    emily_gives_half = emily_new_total / 2
    emily_final_total = emily_new_total - emily_gives_half - 1
    result = emily_final_total
    return result

print(solution())