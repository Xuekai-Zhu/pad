def solution():
    # Define the angle A and the ratio between B and C
    A = 60
    B_to_C_ratio = 2

    # Calculate the sum of the angles of a triangle
    total_angle = 180

    # Calculate the angle C
    C = (total_angle - A) / (1 + B_to_C_ratio)

    # Calculate the angle B
    B = B_to_C_ratio * C
    result = B
    return result

print(solution())