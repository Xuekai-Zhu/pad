def solution():
    """Ford owns a garden and he grows 40 roses every week. He supplies Roses to the local flower shops. 
    The first flower shop orders 20 roses, the second flower shop orders 15 roses, and the third flower shop orders 30 roses per week. 
    How many roses does Ford lack to supply all the flower shops every month?"""
    
    roses_per_week = 40
    roses_first_shop = 20
    roses_second_shop = 15
    roses_third_shop = 30
    
    total_roses_per_week = roses_first_shop + roses_second_shop + roses_third_shop
    roses_lack_per_week = total_roses_per_week - roses_per_week
    
    roses_lack_per_month = roses_lack_per_week * 4
    result = roses_lack_per_month
    
    return result

print(solution())