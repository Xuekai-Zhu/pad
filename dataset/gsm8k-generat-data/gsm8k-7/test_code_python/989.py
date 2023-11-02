def solution():
    caleb_bucket = 7
    cynthia_bucket = 8
    total_gallons = 105

    # Calculate the total number of trips needed
    num_trips = total_gallons / (caleb_bucket + cynthia_bucket)

    result = num_trips
    return result

print(solution())