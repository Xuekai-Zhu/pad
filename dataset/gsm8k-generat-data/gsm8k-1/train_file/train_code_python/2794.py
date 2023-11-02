def solution():
    """Holden's current master bedroom is 309 sq ft and his master bath is 150 sq ft. If he wants to add a home office/personal gym divided space that is twice as large as his bedroom and bathroom, how much sq ft will this new room have?"""
    current_bedroom_sqft = 309
    current_bath_sqft = 150
    new_room_factor = 2
    new_room_sqft = (current_bedroom_sqft + current_bath_sqft) * new_room_factor
    result = new_room_sqft
    return result

print(solution())