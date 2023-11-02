def solution():
    # Calculate the total number of glass panels in the downstairs windows
    downstairs_panels = 6 * 2 * 4

    # Calculate the total number of glass panels in the upstairs windows
    upstairs_panels = 8 * 4

    # Calculate the total number of glass panels in the whole house
    total_panels = downstairs_panels + upstairs_panels
    result = total_panels
    return result

print(solution())