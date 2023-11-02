def solution():
    # Calculate the total amount of flour used
    total_flour = 3 * 8 * 2  # 3 bags, 8 cups each, 2 cups per pound

    # Calculate the total amount of pasta made
    total_pasta = total_flour / 3  # 3 pounds of pasta per 6 cups of flour

    # Calculate the number of drying racks needed
    racks_needed = total_pasta / 3

    # Calculate the number of additional drying racks needed
    additional_racks = racks_needed - 3  # she already has 3 racks

    result = additional_racks
    return result

print(solution())