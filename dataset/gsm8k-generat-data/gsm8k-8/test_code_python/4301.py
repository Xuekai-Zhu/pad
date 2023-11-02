def solution():
    # Define the number of each type of stocking stuffer
    candy_canes = 4
    beanie_babies = 2
    books = 1

    # Calculate the total number of stocking stuffers for one child
    total_stocking_stuffers_per_child = candy_canes + beanie_babies + books

    # Calculate the total number of stocking stuffers for all three children
    total_stocking_stuffers = total_stocking_stuffers_per_child * 3
    result = total_stocking_stuffers
    return result

print(solution())