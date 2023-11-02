def solution():
    """Edmund is buying a new computer and needs to save up $75 before he has enough. He convinces his parents to pay him for extra chores. He normally has to do 12 chores a week. His parents agree to pay him $2 for every extra chore he does during the week. If he does 4 chores a day for two weeks, how much does he earn?"""
    # Define Edmund's savings goal and the payment for each extra chore
    SAVINGS_GOAL = 75
    EXTRA_CHORE_PAYMENT = 2

    # Calculate the number of extra chores Edmund does over two weeks
    num_extra_chores = (4 * 7 * 2) - 12

    # Calculate Edmund's earnings from the extra chores
    extra_chore_earnings = num_extra_chores * EXTRA_CHORE_PAYMENT

    # Calculate the total amount of money Edmund has saved
    total_saved = extra_chore_earnings

    # Check if Edmund has reached his savings goal
    if total_saved >= SAVINGS_GOAL:
        result = SAVINGS_GOAL
    else:
        result = total_saved
    return result

print(solution())