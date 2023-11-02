def solution():
    main_building_shape = "Octagon"
    yield_sign_shape = "Rounded triangle"
    are_shapes_similar = False
    if main_building_shape.lower() in yield_sign_shape.lower():
        are_shapes_similar = True
    if are_shapes_similar:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())