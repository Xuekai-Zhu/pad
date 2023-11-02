def solution():
    # Calculate the total amount of money in Tyrone's piggy bank
    total_money = 2*1 + 1*5 + 0.25*13 + 0.10*20 + 0.05*8 + 0.01*35
    result = round(total_money, 2)  # round to 2 decimal places
    return result

print(solution())