def solution():
    cost_per_notepad = 1.25  # Bart buys notepads for $1.25 each
    total_cost = 10  # Bart spends $10 on notepads
    number_of_notepads = total_cost / cost_per_notepad  # Calculate the number of notepads Bart bought
    pages_per_notepad = 60  # The notepads have 60 pages each

    # Calculate the total number of pages Bart bought
    total_pages = number_of_notepads * pages_per_notepad
    result = total_pages
    return result

print(solution())