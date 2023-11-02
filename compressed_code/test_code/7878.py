def solution():
    
    haircut_price = 30
    perm_price = 40
    dye_price = 60
    dye_cost = 10
    num_haircuts = 4
    num_perms = 1
    num_dyes = 2
    
    
    total_revenue = (num_haircuts * haircut_price) + (num_perms * perm_price) + (num_dyes * (dye_price - dye_cost))
    
    
    total_revenue += 50
    
    result = total_revenue
    
    return result

print(solution())