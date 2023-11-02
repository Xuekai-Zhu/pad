def solution():
    
    total_cost = 10
    notepad_cost = 1.25
    num_notepads = total_cost / notepad_cost
    pages_per_notepad = 60
    total_pages = num_notepads * pages_per_notepad
    result = total_pages
    return result

print(solution())