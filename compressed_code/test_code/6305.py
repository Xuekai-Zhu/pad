def solution():
    
    total_cost = 10
    cost_per_notepad = 1.25
    num_notepads = total_cost / cost_per_notepad
    pages_per_notepad = 60
    total_pages = num_notepads * pages_per_notepad
    result = total_pages
    
    return result

print(solution())