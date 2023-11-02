def solution():
    """Jan buys 1000 feet of cable. She splits it up into 25-foot sections. She gives 1/4 of that to a friend. She then puts half of the rest in storage. How much does she keep on hand?"""
    total_feet = 1000
    section_length = 25
    total_sections = total_feet / section_length
    friend_sections = total_sections / 4
    remaining_sections = total_sections - friend_sections
    storage_sections = remaining_sections / 2
    on_hand_sections = remaining_sections - storage_sections
    on_hand_feet = on_hand_sections * section_length
    result = on_hand_feet
    return result

print(solution())