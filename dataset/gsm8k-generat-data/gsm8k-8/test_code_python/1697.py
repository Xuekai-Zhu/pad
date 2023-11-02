def solution():
    # Define the initial amount in the cookie jar
    initial_amount = 21

    # Doris spent $6, so there is $21 - $6 = $15 left.
    remaining_amount = initial_amount - 6

    # Martha spent half as much as Doris, which is $6 / 2 = $3
    remaining_amount -= 3

    result = remaining_amount
    return result

print(solution())