def solution():
    # Convert Margaret's money to cents
    margaret_cents = 75

    # Add up the total cents for all four people
    total_cents = 70 + margaret_cents + 60 + 60

    # Add up the coins and dimes Bill has separately
    bill_cents = 6 * 10
    guy_cents = 2 * 25 + 10

    # Add the coins and dimes to the total cents
    total_cents += bill_cents + guy_cents

    result = total_cents
    return result

print(solution())