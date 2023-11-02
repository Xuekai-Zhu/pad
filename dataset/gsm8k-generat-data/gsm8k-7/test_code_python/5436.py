def solution():
    num_products = 5
    time_between_products = 5  # in minutes
    make_up_time = 30  # in minutes

    # Calculate the total time spent on facial products
    time_on_products = (num_products - 1) * time_between_products

    # Calculate the total time spent on the full face
    full_face_time = time_on_products + make_up_time
    result = full_face_time
    return result

print(solution())