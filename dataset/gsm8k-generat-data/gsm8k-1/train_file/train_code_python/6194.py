def solution():
    """Mara has 40 crayons and 10 percent of her crayons are pink. Luna has 50 crayons and 20 percent of them are pink. In total how many pink crayons do Mara and Luna have?"""
    mara_crayons = 40
    mara_pink_crayons = mara_crayons * 0.10
    luna_crayons = 50
    luna_pink_crayons = luna_crayons * 0.20
    total_pink_crayons = mara_pink_crayons + luna_pink_crayons
    result = total_pink_crayons
    return result

print(solution())