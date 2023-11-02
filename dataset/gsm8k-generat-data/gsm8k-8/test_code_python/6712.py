def solution():
    hike_duration = 4
    old_shoe_speed = 6
    new_shoe_speed = 2 * old_shoe_speed
    blister_duration = 2
    blister_effect = 2

    # Calculate how many blisters Candace will get with the new shoes
    num_blisters = hike_duration // blister_duration

    # Calculate the speed reduction due to blisters
    blister_reduction = num_blisters * blister_effect

    # Calculate the final speed with the new shoes
    new_shoe_speed -= blister_reduction

    result = new_shoe_speed
    return result

print(solution())