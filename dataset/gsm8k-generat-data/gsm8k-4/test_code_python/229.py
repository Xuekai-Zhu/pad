def solution():
    """Jan buys 1000 feet of cable. She splits it up into 25-foot sections. She gives 1/4 of that to a friend. She then puts half of the rest in storage. How much does she keep on hand?"""
    # Define the total length of cable that Jan buys
    total_cable = 1000

    # Calculate the length of each 25-foot section
    section_length = 25

    # Calculate the number of sections Jan has
    num_sections = total_cable / section_length

    # Calculate the number of sections Jan gives to her friend
    friend_sections = num_sections / 4

    # Calculate the number of sections Jan puts in storage
    storage_sections = (num_sections - friend_sections) / 2

    # Calculate the number of sections Jan keeps on hand
    on_hand_sections = num_sections - friend_sections - storage_sections

    # Calculate the length of cable Jan keeps on hand
    on_hand_cable = on_hand_sections * section_length

    # return the result
    result = on_hand_cable
    return result

print(solution())