def solution():
    """Marissa has 4.5 feet of ribbon that she wants to use to tie some boxes. If 1 foot of ribbon is left after Marissa uses 0.7 feet of ribbon to tie each box, find out how many boxes she tied?"""
    total_ribbon = 4.5
    ribbon_per_box = 0.7
    remaining_ribbon = 1
    boxes_tied = (total_ribbon - remaining_ribbon) / ribbon_per_box
    result = boxes_tied
    return result

print(solution())