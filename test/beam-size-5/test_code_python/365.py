def solution():
    num_seniors = 44
    picture_frame_cost = 20
    logo_cost = 0.2 * picture_frame_cost
    num_pins = 2
    pin_cost = 5
    num_officers = num_seniors / 4
    cord_cost = 12

    # Calculate the total cost of all seniors
    total_cost = (num_seniors * picture_frame_cost) + (num_pins * pin_cost) + (num_officers * cord_cost)
    result = total_cost
    return result

print(solution())