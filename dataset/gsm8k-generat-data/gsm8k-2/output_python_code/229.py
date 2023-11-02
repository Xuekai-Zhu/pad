def solution():
    """Jan buys 1000 feet of cable. She splits it up into 25-foot sections. She gives 1/4 of that to a friend. She then puts half of the rest in storage. How much does she keep on hand?"""
    total_cable_size = 1000
    cable_section_size = 25
    num_sections = total_cable_size / cable_section_size
    sections_given_away = num_sections / 4
    sections_left = num_sections - sections_given_away
    sections_in_storage = sections_left / 2
    sections_on_hand = sections_left - sections_in_storage
    result = sections_on_hand * cable_section_size
    return result

print(solution())