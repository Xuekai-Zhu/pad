def solution():
    # Calculate the total number of glass panels in the whole house
    downstairs_glass_panels = 6 * 2 * 4  # 6 double windows with 2 panels each and 4 panels per window
    upstairs_glass_panels = 8 * 1 * 4  # 8 single windows with 1 panel each and 4 panels per window
    total_glass_panels = downstairs_glass_panels + upstairs_glass_panels
    result = total_glass_panels
    return result

print(solution())