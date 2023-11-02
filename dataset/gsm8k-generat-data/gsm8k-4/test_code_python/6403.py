def solution():
    """An archer needs to practice.  He intends to shoot 200 shots 4 days a week.  He is able to recover 20% of his arrows.  The arrows he uses cost $5.5 per arrow.  His team agrees to pay for 70% of the cost of his arrows.  How much does he spend for arrows a week?"""
    # Define the number of shots per week and the percentage of arrows recovered
    weekly_shots = 200 * 4
    arrow_recovery_percentage = 0.2

    # Calculate the number of arrows used per week and the number of arrows recovered
    arrows_used = weekly_shots
    arrows_recovered = arrows_used * arrow_recovery_percentage

    # Calculate the total cost of the arrows and the cost covered by the team
    total_cost = arrows_used * 5.5
    team_coverage = total_cost * 0.7

    # Calculate the archer's out-of-pocket cost for the arrows
    out_of_pocket_cost = total_cost - team_coverage

    result = out_of_pocket_cost
    return result

print(solution())