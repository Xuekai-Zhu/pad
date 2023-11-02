def solution():
    colors = 4  # The factory makes 4 colors of crayons
    crayons_per_color = 2  # The factory puts 2 of each color crayon in each box
    boxes_per_hour = 5  # The factory produces enough crayons to fill 5 boxes per hour
    hours = 4  # The factory wants to know how many crayons they will produce in 4 hours

    # Calculate the total number of crayons produced per hour
    crayons_per_hour = colors * crayons_per_color * boxes_per_hour

    # Calculate the total number of crayons produced in 4 hours
    total_crayons = crayons_per_hour * hours
    result = total_crayons
    return result

print(solution())