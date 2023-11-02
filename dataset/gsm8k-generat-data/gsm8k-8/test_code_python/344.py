def solution():
    marbles_remaining_after_street = 0.4 * archies_marbles
    marbles_remaining_after_sewer = 0.5 * marbles_remaining_after_street
    marbles_remaining = 20
    marbles_before_sewer = marbles_remaining / marbles_remaining_after_sewer
    archies_marbles = marbles_before_sewer * marbles_remaining_after_street
    result = archies_marbles
    return result

print(solution())