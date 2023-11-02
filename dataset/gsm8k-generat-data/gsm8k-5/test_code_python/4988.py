def solution():
    initial_debt = 40  # Tessa's first debt was $40
    first_payment = initial_debt / 2  # Tessa paid back half of her debt
    second_debt = 10  # Tessa asked for $10 more a few days later

    # Calculate the total amount Tessa owes Greg
    total_debt = initial_debt - first_payment + second_debt
    result = total_debt
    return result

print(solution())