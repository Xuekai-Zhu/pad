def solution():
    # Define that the United States Air Force is part of the military and Dunkin Donuts offers a military discount
    air_force_member = True
    military_discount = True
    # Check if an Air Force member would get a discount at Dunkin Donuts
    if air_force_member and military_discount:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())