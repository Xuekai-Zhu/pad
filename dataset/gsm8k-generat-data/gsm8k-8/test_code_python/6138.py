def solution():
    # Calculate the amount of money Heaven spent
    heaven_spent = 2*5 + 4*5

    # Calculate the amount of money Heaven's brother had left
    brother_money = 100 - heaven_spent

    # Calculate the amount of money Heaven's brother spent on erasers
    eraser_spent = 10*4

    # Calculate the amount of money Heaven's brother spent on highlighters
    highlighters_spent = brother_money - eraser_spent

    result = highlighters_spent
    return result

print(solution())