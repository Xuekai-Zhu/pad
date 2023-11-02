def solution():
    laundry_machine_capacity = 5  # in pounds
    shirts_per_pound = 4
    pants_per_pound = 2
    num_shirts = 20
    num_pants = 20

    # Calculate the total weight of all shirts and pants
    total_weight = (num_shirts / shirts_per_pound) + (num_pants / pants_per_pound)

    # Calculate the number of loads of laundry required
    num_loads = total_weight / laundry_machine_capacity
    result = num_loads
    return result

print(solution())