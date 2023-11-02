def solution():
    """Grandma left $124,600 in her will. She gave half of it to her favorite grandchild, Shelby. The rest was to be evenly divided among the remaining 10 grandchildren. How many dollars did one of the remaining 10 grandchildren receive?"""
    total_inheritance = 124600
    shelby_inheritance = total_inheritance / 2
    remaining_inheritance = total_inheritance - shelby_inheritance
    remaining_grandchildren = 10
    inheritance_per_grandchild = remaining_inheritance / remaining_grandchildren
    result = inheritance_per_grandchild
    
    return result

print(solution())