def solution():
    
    total_inheritance = 124600
    shelby_inheritance = total_inheritance / 2
    remaining_inheritance = total_inheritance - shelby_inheritance
    remaining_grandchildren = 10
    inheritance_per_grandchild = remaining_inheritance / remaining_grandchildren
    result = inheritance_per_grandchild
    
    return result

print(solution())