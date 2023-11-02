def solution():
    # Calculate the number of shots per day
    shots_per_day = 200/4

    # Calculate the number of arrows used in one week (assuming no recovery)
    total_arrows = 7 * shots_per_day

    # Calculate the number of arrows recovered
    arrows_recovered = total_arrows * 0.2

    # Calculate the number of arrows not recovered
    arrows_not_recovered = total_arrows - arrows_recovered

    # Calculate the total cost of arrows
    total_cost = arrows_not_recovered * 5.5

    # Calculate the amount paid by the team
    team_payment = total_cost * 0.7

    # Calculate the amount paid by the archer
    archer_payment = total_cost - team_payment

    result = archer_payment
    return result

print(solution())