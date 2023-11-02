def solution():
    """Holden's current master bedroom is 309 sq ft and his master bath is 150 sq ft.
    If he wants to add a home office/personal gym divided space that is twice as large as his bedroom and bathroom,
    how much sq ft will this new room have?"""
    # Define the current square footage of Holden's master bedroom and bathroom
    CURRENT_BEDROOM_SQFT = 309
    CURRENT_BATHROOM_SQFT = 150

    # Calculate the desired square footage of the new room
    DESIRED_NEW_ROOM_SQFT = (CURRENT_BEDROOM_SQFT + CURRENT_BATHROOM_SQFT) * 2

    # Display the desired square footage of the new room
    result = DESIRED_NEW_ROOM_SQFT
    return result

print(solution())