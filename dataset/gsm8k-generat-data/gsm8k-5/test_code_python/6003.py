def solution():
    # Calculate the time taken for the first part of the journey
    first_time = 30 / 60  # 30 minutes converted to hours
    first_distance = 10 * first_time  # Distance covered at 10 miles per hour

    # Calculate the time taken for the second part of the journey
    second_distance = 15
    second_speed = (second_distance - first_distance) / ((30 + 30) / 60)  # Speed needed to cover 15 miles in 1 hour
    second_time = second_distance / second_speed

    # Calculate the time taken for the final part of the journey
    third_distance = 20
    third_speed = (third_distance - second_distance) / ((30 + second_time) / 60)  # Speed needed to cover 20 miles in remaining time
    third_time = third_distance / third_speed

    # Calculate the total time taken for the whole journey
    total_time = (first_time + second_time + third_time) * 60  # Converted to minutes
    result = total_time
    return result

print(solution())