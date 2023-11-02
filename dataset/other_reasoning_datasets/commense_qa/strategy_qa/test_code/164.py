def solution():
    old_testament = True
    new_testament = False
    daniel_thrown_into_lions_den = True
    
    if daniel_thrown_into_lions_den and old_testament:
        result = "no"
    elif daniel_thrown_into_lions_den and new_testament:
        result = "invalid question"
    else:
        result = "no"
    return result

print(solution())