def solution():
    # Calculate the amount Pete spent
    pete_spent = 4 * 5

    # Calculate the amount Raymond spent
    raymond_spent = (250 - pete_spent - 70)  # 70 cents = 7 dimes

    # Calculate the total amount they spent, in cents
    total_spent = pete_spent + raymond_spent

    # Convert the total amount to dollars
    total_spent_dollars = total_spent/100

    result = int(total_spent)
    return result

print(solution())