def solution():
    # Calculate the number of milkshakes that Blake can make
    milkshakes = min(72//4, 192//12)  # he can only make as many milkshakes as the limiting ingredient allows

    # Calculate the amount of milk left over
    leftover_milk = 72 - (milkshakes * 4)  # he used 4 ounces of milk for each milkshake
    result = leftover_milk
    return result

print(solution())