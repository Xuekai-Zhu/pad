def solution():
    """An ice cream vendor has 50 chocolate-flavored ice creams and 54 mango-flavored ice creams in his cart. If he sold 3/5 of the chocolate-flavored ice creams and 2/3 of the mango-flavored ice creams, how many total ice creams were not sold?"""
    chocolate_ice_creams = 50
    mango_ice_creams = 54
    sold_chocolate_ice_creams = int(0.6 * chocolate_ice_creams)
    sold_mango_ice_creams = int(0.3333333333333333 * mango_ice_creams) #approximating 2/3
    unsold_ice_creams = chocolate_ice_creams + mango_ice_creams - sold_chocolate_ice_creams - sold_mango_ice_creams
    result = unsold_ice_creams
    return result

print(solution())