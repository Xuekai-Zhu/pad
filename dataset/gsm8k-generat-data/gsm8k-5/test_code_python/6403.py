def solution():
    # Calculate the total number of arrows used in a week
    arrows_per_day = 200 / 4  # The archer shoots 200 arrows over 4 days
    arrows_used = arrows_per_day * 7  # The archer shoots arrows for 7 days in a week
    arrows_recovered = arrows_used * 0.2  # The archer recovers 20% of the arrows he shoots
    net_arrows_used = arrows_used - arrows_recovered  # The archer uses this many arrows
    arrow_cost = 5.5  # The cost of each arrow is $5.5

    # Calculate the amount spent by the archer on arrows per week
    total_cost = net_arrows_used * arrow_cost  # This is the total cost of the arrows
    team_coverage = 0.7  # The team pays for 70% of the cost of arrows
    archer_cost = total_cost * (1 - team_coverage)  # This is the amount the archer needs to pay
    result = archer_cost
    return result

print(solution())