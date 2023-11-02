def solution():
    """Pete and Raymond each receive $2.50 from their grandmother. Pete saves his money and only spends 4 nickels. Raymond spends his money at the arcade games but still has 7 dimes left. How much did Pete and Raymond spent altogether, in cents?"""
    # Define the amount of money Pete received and spent
    pete_money = 250  # in cents
    pete_spent = 20   # in cents (4 nickels)

    # Calculate the amount of money Raymond spent
    raymond_spent = pete_money - pete_spent - 70   # in cents (7 dimes)

    # Calculate the total amount spent by both
    total_spent = pete_spent + raymond_spent

    # Display the total amount spent
    result = total_spent
    return result

print(solution())