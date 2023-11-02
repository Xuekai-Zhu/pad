def solution():
    capital_a = 300
    capital_b = 200
    interest_rate_a = 0.3
    interest_rate_b = 0.5

    # Calculate the interest earned in scheme A and B after a year
    interest_a = capital_a * interest_rate_a
    interest_b = capital_b * interest_rate_b

    # Calculate the total amount of money investor will have in scheme A and B after a year
    total_a = capital_a + interest_a
    total_b = capital_b + interest_b

    # Calculate the difference in amount of money between scheme A and B after a year
    difference = total_a - total_b
    result = difference
    return result

print(solution())