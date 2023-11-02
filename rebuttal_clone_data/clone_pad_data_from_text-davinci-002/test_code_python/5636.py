def solution():
    eggs = 3
    pancakes = 2
    mugs_of_cocoa = 2
    tax = 1
    total_cost = eggs + pancakes + mugs_of_cocoa + tax
    additional_cost = pancakes + mugs_of_cocoa
    total_cost = total_cost + additional_cost
    result = 15 - total_cost
    
    return result

print(solution())