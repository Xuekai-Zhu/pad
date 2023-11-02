def solution():
    """An ice cream vendor has 50 chocolate-flavored ice creams and 54 mango-flavored ice creams in his cart. 
    If he sold 3/5 of the chocolate-flavored ice creams and 2/3 of the mango-flavored ice creams, how many total ice creams were not sold?"""
    chocolate_ice_creams = 50
    mango_ice_creams = 54
    chocolate_sold = int(chocolate_ice_creams * 3/5)
    mango_sold = int(mango_ice_creams * 2/3)
    total_sold = chocolate_sold + mango_sold
    total_not_sold = chocolate_ice_creams + mango_ice_creams - total_sold
    result = total_not_sold
    return result

print(solution())