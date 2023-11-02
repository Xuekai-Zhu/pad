def solution():
    kitchen_width = 12
    kitchen_length = 16
    wall_height = 10
    primer_coats = 1
    paint_coats = 2
    painting_rate = 40  # square feet per hour

    # Calculate the total area of all four walls
    wall_area = 2 * (kitchen_width + kitchen_length) * wall_height

    # Calculate the total area that needs to be painted (including primer and paint coats)
    total_area = wall_area * (primer_coats + paint_coats)

    # Calculate the total time needed to paint the entire kitchen
    total_time = total_area / painting_rate
    result = total_time
    return result

print(solution())