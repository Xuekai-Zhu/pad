def solution():
    
    # Define the speed of a whirligig and the ratio of the two spins
    whirligig_to_thingamabob_ratio = 5
    whatchamacallit_to_whatchamacallit_ratio = 11

    # Calculate the speed of a whatchamacallit
    whatchamacallit_speed = 121 / (whatchamacallit_to_thingamabob_ratio + 1)

    # Calculate the speed of a whirligig
    whirligig_speed = whirligig_to_thingamabob_ratio * whatchamacallit_speed

    # Display the speed of a whirligig
    result = whirligig_speed
    return result

print(solution())