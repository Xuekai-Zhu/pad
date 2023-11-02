def solution():
    total_income = 8000  # Nigella earns $8000 in a month
    base_salary = 3000  # Nigella's base salary is $3000
    commission_rate = 0.02  # Nigella earns 2% commission on every house she sells
    commission_income = total_income - base_salary  # Calculate Nigella's commission income
    houses_sold = 3  # Nigella sells 3 houses in a month

    # Calculate the total cost of the houses Nigella sold
    houseB_cost = (commission_income / houses_sold) * 3  # House B costs three times as much as House A
    houseC_cost = ((commission_income / houses_sold) + 110000) * 2  # House C costs twice as much as House A minus $110,000
    houseA_cost = (commission_income / houses_sold) - (houseB_cost + houseC_cost)  # Calculate the cost of House A

    result = houseA_cost
    return result

print(solution())