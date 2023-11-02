def solution():
    feet_bought = 50
    feet_used = feet_bought / 5
    feet_given = feet_bought - feet_used
    feet_received = feet_given / 2
    sections_cut = feet_received / 2
    result = sections_cut
    return result

print(solution())