def solution():
    """Brianne saves $10 in January. Each month, she saves twice as much as her previous month's savings. How much will she save in May?"""
    # Define the initial saving amount and the month counter
    saving = 10
    month = 1

    # Calculate the savings for each subsequent month
    while month < 5:
        saving *= 2
        month += 1

    # Display the savings for May
    result = saving
    return result

print(solution())