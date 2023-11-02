def solution():
    """In a field of 500 clovers, 20% have four leaves and one quarter of these are purple clovers. Assuming these proportions are exactly correct, how many clovers in the field are both purple and four-leaved?"""
    total_clovers = 500
    four_leaves_percent = 20
    purple_percent = 25
    
    # number of four-leaved clovers
    four_leaves = (four_leaves_percent / 100) * total_clovers
    
    # number of purple clovers among the four-leaved clovers
    purple_clovers = (purple_percent / 100) * four_leaves
    
    # number of clovers that are both purple and four-leaved
    result = purple_clovers
    return result

print(solution())