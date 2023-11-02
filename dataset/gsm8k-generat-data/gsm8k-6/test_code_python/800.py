def solution():
    # Calculate the cost of Sandy's order
    cost = (3*2) + (2*3) + (2*1.5) + (2*1)  # cost of 3 cappuccinos, 2 iced teas, 2 cafe lattes, and 2 espressos
    change = 20 - cost  # change received from a $20 bill

    result = change
    return result

print(solution())