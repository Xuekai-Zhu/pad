def solution():
    """Dale and Andrew had breakfast at a cafe. A slice of toast costs £1, and eggs cost £3 each. Dale had 2 slices of toast and 2 eggs. Andrew had 1 slice of toast and 2 eggs. How much did their breakfast cost?"""
    toast_cost = 1
    egg_cost = 3

    dale_toast = 2
    dale_eggs = 2
    dale_total = (dale_toast * toast_cost) + (dale_eggs * egg_cost)

    andrew_toast = 1
    andrew_eggs = 2
    andrew_total = (andrew_toast * toast_cost) + (andrew_eggs * egg_cost)

    total_cost = dale_total + andrew_total
    result = total_cost
    return result

print(solution())