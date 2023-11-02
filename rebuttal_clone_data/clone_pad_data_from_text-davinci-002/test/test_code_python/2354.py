def solution ():
    flour_used = 1.25
    biscuits_made = 9
    guests = 18
    biscuits_needed = guests * 2
    flour_needed = (flour_used / biscuits_made) * biscuits_needed
    result = flour_needed
    return result

print(solution())