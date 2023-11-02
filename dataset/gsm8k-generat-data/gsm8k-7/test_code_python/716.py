def solution():
    lance_cents = 70
    margaret_dollars = 0.75
    guy_cents = 60
    bill_cents = 60

    # Convert Margaret's dollars to cents
    margaret_cents = int(margaret_dollars * 100)

    # Calculate the total number of cents
    total_cents = lance_cents + margaret_cents + guy_cents + bill_cents
    result = total_cents
    return result

print(solution())