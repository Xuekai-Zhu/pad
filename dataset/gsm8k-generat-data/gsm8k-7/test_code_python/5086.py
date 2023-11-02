def solution():
    evening_ticket_cost = 10
    combo_cost = 10

    # Calculate the cost of evening ticket and combo
    evening_cost = evening_ticket_cost + combo_cost

    # Calculate the cost of noon ticket and combo
    noon_ticket_cost = evening_ticket_cost * 0.8
    noon_combo_cost = combo_cost * 0.5
    noon_cost = noon_ticket_cost + noon_combo_cost

    # Calculate the savings from going to the earlier movie
    savings = evening_cost - noon_cost
    result = savings
    return result

print(solution())