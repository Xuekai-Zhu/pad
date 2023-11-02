def solution():
    cattle_to_move = 400  # The rancher needs to move 400 head of cattle
    truck_capacity = 20  # The animal transport truck holds 20 head of cattle
    distance_to_cover = 60  # The rancher needs to drive 60 miles to higher ground
    speed = 60  # The rancher can travel at 60 miles per hour

    # Calculate the number of trips the rancher needs to make
    trips = cattle_to_move / truck_capacity

    # Calculate the total driving time
    total_driving_time = (distance_to_cover * trips) / speed
    result = total_driving_time
    return result

print(solution())