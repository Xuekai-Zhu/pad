def solution():
    """Sanya can wash 7 bath towels in one wash, which will take 1 hour. She only has 2 hours in a day to do this task. If she has 98 bath towels, how many days will she need to wash all of them?"""
    # Calculate the number of wash cycles needed
    wash_cycles = 98 / 7

    # Calculate the number of days needed to complete the task
    days_needed = wash_cycles / 2

    # Display the number of days needed
    result = days_needed
    return result

print(solution())