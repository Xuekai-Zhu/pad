def solution():
    """Jan buys 1000 feet of cable.  She splits it up into 25-foot sections.  She gives 1/4 of that to a friend.  She then puts half of the rest in storage. How much does she keep on hand?"""
    # Define the total amount of cable Jan buys and the length of each section
    total_cable = 1000
    cable_section = 25

    # Calculate the number of cable sections Jan has
    num_sections = total_cable / cable_section

    # Calculate the number of sections Jan gives to her friend
    friend_sections = num_sections / 4

    # Calculate the remaining number of sections
    remaining_sections = num_sections - friend_sections

    # Calculate the number of sections Jan puts in storage
    storage_sections = remaining_sections / 2

    # Calculate the number of sections Jan keeps on hand
    hand_sections = remaining_sections - storage_sections

    # Calculate the length of cable Jan keeps on hand
    hand_cable = hand_sections * cable_section

    # Display the length of cable Jan keeps on hand
    result = hand_cable
    return result

print(solution())