def solution():
    num_friends = 6
    beads_per_bracelet = 8
    total_beads_needed = num_friends * beads_per_bracelet
    beads_remaining = 36 - total_beads_needed
    result = beads_remaining
    return result

print(solution())