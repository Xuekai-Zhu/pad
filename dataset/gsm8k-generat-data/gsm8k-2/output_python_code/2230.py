def solution():
    """A married couple and their 6 children are ordering some pizza. If the couple want 3 slices each and the children want 1 slice each, how many 4-slice pizzas should they order?"""
    couple_slices = 6
    children_slices = 6
    total_slices = couple_slices * 2 + children_slices
    pizzas = total_slices // 4
    if total_slices % 4 != 0:
        pizzas += 1

    result = pizzas
    return result

print(solution())