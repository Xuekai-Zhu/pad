def solution():
    """Holden's current master bedroom is 309 sq ft and his master bath is 150 sq ft. If he wants to add a home office/personal gym divided space that is twice as large as his bedroom and bathroom, how much sq ft will this new room have?"""
    bedroom_size = 309
    bathroom_size = 150
    new_room_size = 2 * (bedroom_size + bathroom_size)
    result = new_room_size
    return result

print(solution())