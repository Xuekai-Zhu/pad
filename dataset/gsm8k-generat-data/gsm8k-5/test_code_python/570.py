def solution():
    # Calculate the total value of money thrown into the pond
    total_value = (5*10) + (3*25) + (8*5) + (60*1)  # 5 dimes = 50 cents, 3 quarters = 75 cents, 8 nickels = 40 cents, 60 pennies = 60 cents

    # Subtract the value of the quarter that Eric took out
    total_value -= 25

    result = total_value
    return result

print(solution())