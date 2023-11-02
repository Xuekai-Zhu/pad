def solution():
    radius = 14 * 12  # in inches
    diameter = 2 * radius
    pencil_length = 6

    # Calculate the number of pencils that can fit end-to-end across the diameter
    num_pencils = diameter / pencil_length
    result = int(num_pencils)
    return result

print(solution())