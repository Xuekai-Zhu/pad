def solution():
    cost_per_notepad = 1.25
    total_cost = 10.0

    # Calculate the total number of notepads Bart bought
    total_notepads = total_cost / cost_per_notepad

    # Calculate the total number of pages Bart bought
    num_pages = total_notepads * 60
    result = num_pages
    return result

print(solution())