def solution():
    cost = 30  # John pays $30 for the heating pad
    uses_per_week = 3  # John uses the heating pad 3 times per week
    weeks = 2  # John uses the heating pad for 2 weeks

    # Calculate the total number of uses
    total_uses = uses_per_week * weeks

    # Calculate the cost per use
    cost_per_use = cost / total_uses
    result = cost_per_use
    return result

print(solution())