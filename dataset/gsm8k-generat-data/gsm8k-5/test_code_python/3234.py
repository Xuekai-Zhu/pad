def solution():
    total_inheritance = 124600  # Grandma left $124,600 in her will
    inheritance_to_shelby = total_inheritance / 2  # Shelby received half of the total inheritance
    remaining_inheritance = total_inheritance - inheritance_to_shelby  # The remaining inheritance is divided among 10 grandchildren
    inheritance_per_grandchild = remaining_inheritance / 10  # The remaining inheritance is divided evenly among 10 grandchildren
    result = inheritance_per_grandchild
    return result

print(solution())