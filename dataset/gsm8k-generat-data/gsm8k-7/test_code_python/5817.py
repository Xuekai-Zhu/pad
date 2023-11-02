def solution():
    neighborhood_a_homes = 10
    neighborhood_a_boxes = 2
    neighborhood_b_homes = 5
    neighborhood_b_boxes = 5
    box_price = 2

    # Calculate the total revenue from neighborhood A
    neighborhood_a_revenue = neighborhood_a_homes * neighborhood_a_boxes * box_price

    # Calculate the total revenue from neighborhood B
    neighborhood_b_revenue = neighborhood_b_homes * neighborhood_b_boxes * box_price

    # Determine which neighborhood has the higher revenue
    if neighborhood_a_revenue > neighborhood_b_revenue:
        result = neighborhood_a_revenue
    else:
        result = neighborhood_b_revenue

    return result

print(solution())