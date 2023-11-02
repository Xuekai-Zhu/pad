def solution():
    # Calculate the total number of 25-foot sections that Jan has
    total_sections = 1000 / 25

    # Calculate the number of sections Jan gives to her friend
    given_sections = total_sections / 4

    # Calculate the remaining sections after giving some to her friend
    remaining_sections = total_sections - given_sections

    # Calculate the number of sections Jan puts in storage
    storage_sections = remaining_sections / 2

    # Calculate the number of sections Jan keeps on hand
    on_hand_sections = remaining_sections - storage_sections
    result = on_hand_sections

    return result

print(solution())