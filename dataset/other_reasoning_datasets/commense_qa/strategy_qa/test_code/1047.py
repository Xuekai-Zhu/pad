def solution():
    # Check if tibia is necessary to play ice hockey
    tibia_necessary = True
    legs_necessary = True
    ice_skates_require_legs = True
    
    if tibia_necessary and legs_necessary and ice_skates_require_legs:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())