def solution():
    # Define whether the Toronto Star has a classifieds section and whether readers can advertise their own labor or services
    toronto_star_has_classifieds = True
    readers_can_advertise_services = True
    # Check if someone can sell their time through the Toronto Star
    if toronto_star_has_classifieds and readers_can_advertise_services:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())