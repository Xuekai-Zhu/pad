def solution():
    doris_spent = 6
    martha_spent = doris_spent / 2
    total_left = 15

    # Calculate the total amount of money spent
    total_spent = doris_spent + martha_spent

    # Calculate the initial amount of money in the jar
    initial_amount = total_spent + total_left
    result = initial_amount
    return result

print(solution())