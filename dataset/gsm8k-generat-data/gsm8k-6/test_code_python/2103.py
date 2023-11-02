def solution():
    # Calculate the total area of the sandbox
    sandbox_area = 40*40  # each side of the square is 40 inches long

    # Calculate the total number of bags of sand required to fill the sandbox
    sand_per_unit_area = 30/80  # a 30-pound bag of sand can fill 80 square inches
    total_sand_required = sandbox_area * sand_per_unit_area

    result = total_sand_required
    return result

print(solution())