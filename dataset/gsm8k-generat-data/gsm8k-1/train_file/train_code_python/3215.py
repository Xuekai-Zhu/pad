def solution():
    """For Mother's Day last year, Kyle picked a dozen roses from his garden, but this year, he was only able to pick half the number of roses. 
    If Kyle wants to give his mother a bouquet with twice as many roses as last year and the grocery store sells one rose for $3, how much would Kyle have to spend?"""
    last_year_roses = 12
    this_year_roses = last_year_roses / 2
    double_roses = last_year_roses * 2
    total_roses = this_year_roses + double_roses
    
    cost_per_rose = 3
    total_cost = total_roses * cost_per_rose
    result = total_cost
    
    return result

print(solution())