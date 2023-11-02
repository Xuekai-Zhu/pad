def solution():
    """Thomas has been saving $40 in the bank every month for six years. His friend Joseph has been saving 2/5 times less money per month. How much money are they having in their savings account altogether?"""
    # Define Thomas' saving amount and duration
    thomas_saving = 40
    thomas_duration = 6 * 12  # 6 years * 12 months

    # Calculate the total amount Thomas has saved
    thomas_total = thomas_saving * thomas_duration

    # Calculate Joseph's saving amount
    joseph_saving = thomas_saving * (3/5)

    # Calculate the total amount Joseph has saved
    joseph_total = joseph_saving * thomas_duration

    # Calculate the total amount both of them have saved
    total_savings = thomas_total + joseph_total

    # Display the total savings
    result = total_savings
    return result

print(solution())