def solution():
    """There are 45 children in a classroom. One-third of them are girls. How many boys are in the classroom?"""
    total_children = 45
    girls = total_children / 3
    boys = total_children - girls
    result = boys
    return result

print(solution())