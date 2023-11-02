def solution():
    # Define the distances traveled on each leg of the trip
    leg1_distance = first_destination
    leg2_distance = 2 * leg1_distance
    leg3_distance = 40
    leg4_distance = 2 * (leg1_distance + leg2_distance + leg3_distance)

    # Calculate the total distance traveled
    total_distance = leg1_distance + leg2_distance + leg3_distance + leg4_distance
    result = total_distance
    return result

print(solution())