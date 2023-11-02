def solution():
    # Calculate the amount of money Pete spent
    pete_spent = 4 * 5  # Pete spends 4 nickels

    # Calculate the amount of money Raymond spent
    raymond_spent = (250 - 7 * 10)  # Raymond spends his $2.50 but has 7 dimes left

    # Calculate the total amount of money spent by both of them
    total_spent = pete_spent + raymond_spent

    # Convert the total amount of money spent to cents
    total_spent_cents = total_spent * 100

    result = total_spent_cents
    return result

print(solution())