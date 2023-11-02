def solution():
    # Cost of one sandwich with one slice of each protein
    sandwich_cost = 0.15 + 0.25 + 0.35

    # Convert sandwich cost to cents
    sandwich_cost_cents = sandwich_cost * 100

    result = sandwich_cost_cents
    return result

print(solution())