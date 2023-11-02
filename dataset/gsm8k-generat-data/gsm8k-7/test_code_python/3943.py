def solution():
    initial_necklaces = 10
    initial_earrings = 15
    added_necklaces = 10
    added_earrings = (2/3)*initial_earrings
    mother_earrings = (1/5)*added_earrings

    # Calculate the total number of necklaces Jessy has
    total_necklaces = initial_necklaces + added_necklaces

    # Calculate the total number of earrings Jessy has
    total_earrings = initial_earrings + added_earrings + mother_earrings

    # Calculate the total number of jewelry pieces Jessy has
    total_jewelry = total_necklaces + total_earrings
    result = total_jewelry
    return result

print(solution())