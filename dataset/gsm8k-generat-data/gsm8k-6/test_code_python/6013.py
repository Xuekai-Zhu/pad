def solution():
    # Calculate the amount of a 20% tip
    # First, find the total bill without the tip by subtracting the tip amount from the bill amount
    bill_without_tip = 42 / 0.15  # Melisa added a 15% tip of $42, so the bill amount without the tip is $280
    # Then, calculate the amount of a 20% tip by multiplying the bill amount without the tip by 0.20
    tip_amount = bill_without_tip * 0.20
    result = tip_amount
    return result

print(solution())