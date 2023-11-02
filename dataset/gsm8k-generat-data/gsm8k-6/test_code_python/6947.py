def solution():
    # Calculate the total number of bugs eaten
    gecko_bugs = 12
    lizard_bugs = gecko_bugs / 2
    frog_bugs = lizard_bugs * 3
    toad_bugs = frog_bugs * 1.5
    total_bugs = gecko_bugs + lizard_bugs + frog_bugs + toad_bugs
    result = total_bugs
    return result

print(solution())