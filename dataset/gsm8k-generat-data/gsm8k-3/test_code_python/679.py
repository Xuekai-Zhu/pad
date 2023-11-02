def solution():
    """Bart buys $10 of notepads for $1.25 each. They have 60 pages each. How many pages did he buy?"""
    # Define the cost per notepad and the number of notepads purchased
    COST_PER_NOTEPAD = 1.25
    NUM_NOTEPADS = 10 / COST_PER_NOTEPAD

    # Calculate the total number of pages purchased
    TOTAL_PAGES = NUM_NOTEPADS * 60

    # Display the total number of pages purchased
    result = TOTAL_PAGES
    return result

print(solution())