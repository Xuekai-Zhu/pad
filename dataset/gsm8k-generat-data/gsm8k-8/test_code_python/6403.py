def solution():
    # Calculate the total number of shots per week
    total_shots = 200 * 4

    # Calculate the total number of arrows used per week
    arrows_used = total_shots * 0.8

    # Calculate the total cost of arrows per week
    arrow_cost = arrows_used * 5.5

    # Calculate the amount that his team will pay
    team_payment = 0.7 * arrow_cost

    # Calculate the amount he will pay
    archer_payment = arrow_cost - team_payment
    result = archer_payment
    return result

print(solution())