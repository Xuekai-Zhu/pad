def solution():
    gallons1 = 10
    price1_per_gallon = 2.00
    total1 = gallons1 * price1_per_gallon

    price2_per_gallon = price1_per_gallon + 1.00
    gallons2 = 10
    total2 = gallons2 * price2_per_gallon

    total_spent = total1 + total2
    result = total_spent
    return result

print(solution())