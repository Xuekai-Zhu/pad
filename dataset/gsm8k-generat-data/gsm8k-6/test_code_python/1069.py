def solution():
    # Calculate the total value of Maria's piggy bank before her mom gives her 5 quarters
    total_value = (4 * 0.10) + (4 * 0.25) + (7 * 0.05)  # 4 dimes = 0.40, 4 quarters = 1.00, 7 nickels = 0.35
    
    # Calculate the total value of Maria's piggy bank after her mom gives her 5 quarters
    total_value += 5 * 0.25  # each quarter is worth 0.25
    
    result = total_value
    return result

print(solution())