def solution():
    """Sanya can wash 7 bath towels in one wash, which will take 1 hour. She only has 2 hours in a day to do this task. If she has 98 bath towels, how many days will she need to wash all of them?"""
    # Calculate the number of bath towel washes needed to wash all towels
    total_washes = 98 / 7

    # Calculate the number of days needed to complete all washes
    days_needed = total_washes / 2

    # Round up to ensure Sanya has enough time to complete all washes within the given deadline
    result = math.ceil(days_needed)
    return result

print(solution())