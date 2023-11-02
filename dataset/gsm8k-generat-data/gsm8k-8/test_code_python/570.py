def solution():
    # Calculate the total amount of money put into the pond
    total_cents = 5 * 10 + 3 * 25 + 8 * 5 + 60

    # Subtract the value of Eric's quarter from the total
    total_cents -= 25

    result = total_cents
    return result

print(solution())