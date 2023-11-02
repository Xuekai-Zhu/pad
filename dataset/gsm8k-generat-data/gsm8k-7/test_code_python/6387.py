def solution():
    floor_length = 10
    floor_width = 8
    carpet_side = 4

    # Calculate the area of the rectangular floor
    floor_area = floor_length * floor_width

    # Calculate the area of one square carpet
    carpet_area = carpet_side ** 2

    # Calculate the number of carpet squares needed to cover the floor
    num_carpets = (floor_length // carpet_side) * (floor_width // carpet_side)

    # Calculate the area of the uncovered part of the floor
    uncovered_area = floor_area - (num_carpets * carpet_area)
    result = uncovered_area
    return result

print(solution())