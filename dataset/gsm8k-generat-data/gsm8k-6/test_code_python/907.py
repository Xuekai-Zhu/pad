def solution():
    # Calculate the number of pallets of different paper products received
    towels_pallets = 20 * (1/2)  # half were paper towels
    tissues_pallets = 20 * (1/4)  # a quarter were tissues
    plates_pallets = 20 * (1/5)  # a fifth were paper plates
    cups_pallets = 20 - towels_pallets - tissues_pallets - plates_pallets  # the rest were paper cups
    result = cups_pallets
    return result

print(solution())