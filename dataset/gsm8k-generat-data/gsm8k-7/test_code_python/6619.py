def solution():
    num_cattle = 400
    cattle_per_truck = 20
    distance = 60
    speed = 60

    # Calculate the total number of truckloads needed to transport all cattle
    num_truckloads = num_cattle // cattle_per_truck
    if num_cattle % cattle_per_truck != 0:
        num_truckloads += 1

    # Calculate the total driving time
    total_time = distance / speed * num_truckloads
    result = total_time
    return result

print(solution())