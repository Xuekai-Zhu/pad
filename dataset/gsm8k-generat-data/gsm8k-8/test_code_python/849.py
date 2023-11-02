def solution():
    # Define the initial number of balloons
    num_balloons = 200

    # Calculate the number of balloons that have blown up after half an hour
    half_hour_blow_up = num_balloons // 5

    # Calculate the number of balloons that blow up after another hour
    remaining_balloons = num_balloons - half_hour_blow_up
    hour_blow_up = 2 * half_hour_blow_up
    remaining_balloons -= hour_blow_up

    result = remaining_balloons
    return result

print(solution())