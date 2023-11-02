def solution():
    # Find the total number of children between John and Yasmin
    total_children = 6 / 2  # since Gabriel has 6 grandkids and John has twice the number of children Yasmin has
    
    # Divide the total children in half to find how many Yasmin has
    yasmin_children = total_children / 2
    
    result = yasmin_children
    return result

print(solution())