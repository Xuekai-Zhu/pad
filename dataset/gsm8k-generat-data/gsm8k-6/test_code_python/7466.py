def solution():
    # Calculate the annual cost of Janet's clarinet lessons
    clarinet_cost = 40 * 3 * 52  # $40/hour for 3 hours/week for 52 weeks

    # Calculate the annual cost of Janet's piano lessons
    piano_cost = 28 * 5 * 52  # $28/hour for 5 hours/week for 52 weeks

    # Find the difference in cost between piano and clarinet lessons
    difference = piano_cost - clarinet_cost
    result = difference
    return result

print(solution())