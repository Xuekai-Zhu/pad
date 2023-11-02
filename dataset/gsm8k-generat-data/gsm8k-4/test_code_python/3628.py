def solution():
    """Edmund is buying a new computer and needs to save up $75 before he has enough. He convinces his parents to pay him for extra chores. He normally has to do 12 chores a week. His parents agree to pay him $2 for every extra chore he does during the week. If he does 4 chores a day for two weeks, how much does he earn?"""
    # Define the target savings and the regular chores
    target_savings = 75
    regular_chores = 12

    # Define the extra chores per week, the payment per extra chore, and the number of weeks
    extra_chores = 4 * 7 - regular_chores
    payment_per_chore = 2
    weeks = 2

    # Calculate the total extra earnings
    extra_earnings = extra_chores * payment_per_chore * weeks

    # Display the result
    result = extra_earnings
    return result

print(solution())