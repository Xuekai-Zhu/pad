def solution():
    """Dale and Andrew had breakfast at a cafe. A slice of toast costs £1, and eggs cost £3 each. Dale had 2 slices of toast and 2 eggs. Andrew had 1 slice of toast and 2 eggs. How much did their breakfast cost?"""
    cost_of_toast = 1
    cost_of_egg = 3
    Dale_toast = 2
    Dale_eggs = 2
    Andrew_toast = 1
    Andrew_eggs = 2
    Dale_cost = Dale_toast * cost_of_toast + Dale_eggs * cost_of_egg
    Andrew_cost = Andrew_toast * cost_of_toast + Andrew_eggs * cost_of_egg
    result = Dale_cost + Andrew_cost
    return result

print(solution())