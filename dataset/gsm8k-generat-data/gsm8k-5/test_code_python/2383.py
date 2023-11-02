def solution():
    raquel_money = 40  # Raquel has $40
    nataly_money = raquel_money * 3  # Nataly has three times as much money as Raquel
    tom_money = nataly_money / 4  # Tom has a quarter as much money as Nataly

    # Calculate the total money that Tom, Raquel, and Nataly have combined
    total_money = raquel_money + nataly_money + tom_money
    result = total_money
    return result

print(solution())