def solution():
    # Calculate the total distance of Rick's road trip
    first_destination = 1  # distance to first destination (in arbitrary units)
    second_destination = 2 * first_destination  # distance to second destination (twice the distance to first destination)
    third_destination = 40  # distance to third destination (40 miles)
    fourth_destination = 2 * (first_destination + second_destination + third_destination)  # distance to final destination (twice the distance of all other legs combined)
    total_distance = first_destination + second_destination + third_destination + fourth_destination
    result = total_distance
    return result

print(solution())