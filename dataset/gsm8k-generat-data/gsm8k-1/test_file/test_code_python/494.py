def solution():
    """Brianne and Ashley make greek orange pie. Ashley brought five boxes with ten oranges in each box, while Brianne brought 20 more oranges than Ashley. If one greek orange pie needs three oranges, how many greek orange pies can they make?"""
    ashley_oranges = 5 * 10
    brianne_oranges = ashley_oranges + 20
    
    total_oranges = ashley_oranges + brianne_oranges
    
    pies = total_oranges // 3
    
    result = pies
    return result

print(solution())