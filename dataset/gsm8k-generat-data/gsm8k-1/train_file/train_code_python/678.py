def solution():
    """Bart buys $10 of notepads for $1.25 each. They have 60 pages each. How many pages did he buy?"""
    total_cost = 10
    cost_per_notepad = 1.25
    num_notepads = total_cost / cost_per_notepad
    pages_per_notepad = 60
    total_pages = num_notepads * pages_per_notepad
    result = total_pages
    
    return result

print(solution())