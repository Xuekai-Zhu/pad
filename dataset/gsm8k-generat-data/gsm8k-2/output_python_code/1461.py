def solution():
    """A candy store uses food colouring in various candies. Each lollipop uses 5ml of food colouring, and each hard candy also needs food colouring. In one day, the candy store makes 100 lollipops and 5 hard candies. They do not use food colouring in anything else. The store has used 600ml of food colouring by the end of the day. How much food colouring, in millilitres, does each hard candy need?"""
    lollipop_coloring = 5
    total_lollipops = 100
    hard_candies = 5
    total_coloring_used = 600
    total_lollipop_coloring = lollipop_coloring * total_lollipops
    hard_candy_coloring = (total_coloring_used - total_lollipop_coloring) / hard_candies
    result = hard_candy_coloring
    return result

print(solution())