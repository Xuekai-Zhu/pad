def solution():
    """Brianne saves $10 in January. Each month, she saves twice as much as her previous month's savings. How much will she save in May?"""
    # Define Brianne's initial savings and the multiplier
    savings = 10
    multiplier = 2

    # Calculate Brianne's savings for each month
    for i in range(4):
        savings *= multiplier

    # Display Brianne's savings for May
    result = savings
    return result

print(solution())