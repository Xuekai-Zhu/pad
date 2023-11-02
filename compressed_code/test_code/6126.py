def solution():
    
    emily_marbles = 6
    megan_marbles = emily_marbles * 2
    emily_new_total = emily_marbles + megan_marbles
    emily_gives_half = emily_new_total / 2
    emily_final_total = emily_new_total - emily_gives_half - 1
    result = emily_final_total
    return result

print(solution())