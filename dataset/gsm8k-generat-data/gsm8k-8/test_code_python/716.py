def solution():
    # Convert Margaret's amount to cents
    margaret_cents = 75

    # Calculate the total cents for each person
    lance_cents = 70
    guy_cents = 2*25 + 10
    bill_cents = 6*10

    # Calculate the combined total
    total_cents = lance_cents + margaret_cents + guy_cents + bill_cents
    result = total_cents
    return result

print(solution())