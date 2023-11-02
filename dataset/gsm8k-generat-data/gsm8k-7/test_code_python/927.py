def solution():
    num_friends = 20
    num_extra_invites = num_friends

    # Calculate the total number of guests that were invited
    total_invites = num_friends + num_extra_invites

    # Calculate the number of guests that actually showed up
    num_attendees = (total_invites / 2) + num_friends
    
    # Add Ashley to the total number of attendees
    total_attendees = num_attendees + 1
    result = total_attendees
    return result

print(solution())