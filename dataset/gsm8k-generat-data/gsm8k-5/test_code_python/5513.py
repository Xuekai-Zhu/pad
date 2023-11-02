def solution():
    capital_a = 300  # Invested $300 in scheme A
    capital_b = 200  # Invested $200 in scheme B

    # Calculate the returns for each scheme after a year
    return_a = 0.3 * capital_a
    return_b = 0.5 * capital_b

    # Calculate the total amount of money in each scheme after a year
    total_a = capital_a + return_a
    total_b = capital_b + return_b

    # Calculate the difference in money between scheme A and B
    difference = total_a - total_b
    result = difference
    return result

print(solution())