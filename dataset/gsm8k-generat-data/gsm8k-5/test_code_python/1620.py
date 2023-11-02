def solution():
    flour_per_pound = 2  # It takes 2 cups of flour to make each pound of pasta dough
    pounds_of_pasta = (3 * 8) / flour_per_pound  # Michelle uses three 8-cup bags of flour to make pasta
    racks_needed = pounds_of_pasta / 3  # Michelle needs a rack for each three pounds of pasta
    current_racks = 3  # Michelle already owns 3 drying racks

    # Calculate the additional drying racks needed
    additional_racks = racks_needed - current_racks
    result = additional_racks
    return result

print(solution())