def solution():
    initial_amount = 21
    doris_spent = 6
    martha_spent = doris_spent / 2

    # Calculate the total amount spent by both Doris and Martha
    total_spent = doris_spent + martha_spent

    # Calculate the amount left in the cookie jar
    amount_left = initial_amount - total_spent
    result = amount_left
    return result

print(solution())