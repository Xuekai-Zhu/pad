def solution():
    # Define the box office numbers for each movie
    divergent_box_office = 295
    the_ring_box_office = 248
    king_kong_box_office = 550
    # Check if King Kong had the highest box office for Naomi Watts
    if king_kong_box_office > divergent_box_office and king_kong_box_office > the_ring_box_office:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())