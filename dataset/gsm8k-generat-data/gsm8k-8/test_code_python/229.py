def solution():
    # Define the variables
    total_cable = 1000
    section_length = 25
    friend_share = total_cable / 4

    # Calculate the amount of cable Jan keeps after giving some to her friend
    remaining_cable = total_cable - friend_share

    # Calculate the amount of cable Jan puts in storage
    storage_cable = remaining_cable / 2

    # Calculate the amount of cable Jan keeps on hand
    on_hand_cable = remaining_cable - storage_cable

    result = on_hand_cable / section_length
    return result

print(solution())