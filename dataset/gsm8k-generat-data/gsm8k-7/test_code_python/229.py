def solution():
    total_cable = 1000
    section_length = 25
    
    # Calculate the number of sections Jan has
    num_sections = total_cable // section_length
    
    # Calculate the number of sections she gives to her friend
    num_given_sections = num_sections // 4
    
    # Calculate the remaining number of sections after giving to her friend
    remaining_sections = num_sections - num_given_sections
    
    # Calculate the number of sections Jan puts in storage
    storage_sections = remaining_sections // 2
    
    # Calculate the number of sections Jan keeps on hand
    on_hand_sections = remaining_sections - storage_sections
    
    # Calculate the length of cable Jan keeps on hand
    on_hand_cable = on_hand_sections * section_length
    
    result = on_hand_cable
    return result

print(solution())