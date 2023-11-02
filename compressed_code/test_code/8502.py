def solution():
    
    initial_flour = 500
    used_flour = 240
    spilled_flour = (initial_flour - used_flour) / 2
    total_flour = initial_flour - used_flour - spilled_flour
    flour_needed = initial_flour - total_flour
    result = flour_needed
    return result

print(solution())