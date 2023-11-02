def solution():
    # Calculate the total cost of the drinks
    total_cost = (3*2) + (2*3) + (2*1.5) + (2*1)  # Three cappuccinos, two iced teas, two cafe lattes, and two espressos

    # Calculate the change Sandy receives back for a $20 bill
    change = 20 - total_cost
    result = change
    return result

print(solution())