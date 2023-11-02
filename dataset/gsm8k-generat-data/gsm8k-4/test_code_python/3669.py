def solution():
    """An ice cream vendor has 50 chocolate-flavored ice creams and 54 mango-flavored ice creams in his cart. If he sold 3/5 of the chocolate-flavored ice creams and 2/3 of the mango-flavored ice creams, how many total ice creams were not sold?"""
    # Define the initial number of chocolate and mango ice creams
    chocolate_ice_creams = 50
    mango_ice_creams = 54

    # Calculate the number of sold chocolate and mango ice creams
    sold_chocolate_ice_creams = 3/5 * chocolate_ice_creams
    sold_mango_ice_creams = 2/3 * mango_ice_creams

    # Calculate the number of unsold chocolate and mango ice creams
    unsold_chocolate_ice_creams = chocolate_ice_creams - sold_chocolate_ice_creams
    unsold_mango_ice_creams = mango_ice_creams - sold_mango_ice_creams

    # Calculate the total number of unsold ice creams
    total_unsold = unsold_chocolate_ice_creams + unsold_mango_ice_creams

    result = total_unsold
    return result

print(solution())