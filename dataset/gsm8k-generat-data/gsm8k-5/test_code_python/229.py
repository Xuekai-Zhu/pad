def solution():
    total_cable = 1000  # Jan buys 1000 feet of cable
    section_length = 25  # Jan splits the cable into 25-foot sections

    # Calculate the amount of cable Jan gives to her friend
    friend_share = (1/4) * (total_cable // section_length) * section_length

    # Calculate the amount of cable Jan keeps for herself
    remaining_cable = total_cable - friend_share
    storage_share = (1/2) * (remaining_cable // section_length) * section_length

    # Calculate the amount of cable Jan keeps on hand
    on_hand = remaining_cable - storage_share
    result = on_hand
    return result

print(solution())