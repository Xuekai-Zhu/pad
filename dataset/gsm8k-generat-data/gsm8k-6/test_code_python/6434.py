def solution():
    # Calculate the cost of 80 olives
    cost_80_olives = (80/20) * 1.5  # each jar of olives costs $1.5 and he needs 80 olives
    change = 10 - cost_80_olives  # subtract the cost from his $10 budget
    result = change
    return result

print(solution())