def solution():
    
    lollipop_coloring = 5
    total_lollipops = 100
    hard_candies = 5
    total_coloring_used = 600
    total_lollipop_coloring = lollipop_coloring * total_lollipops
    hard_candy_coloring = (total_coloring_used - total_lollipop_coloring) / hard_candies
    result = hard_candy_coloring
    return result

print(solution())