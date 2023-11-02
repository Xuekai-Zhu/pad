def solution():
    # Calculate the number of people who rode in vans
    people_in_vans = 9 * 8  # 9 vans, 8 people in each van

    # Calculate the number of people who rode in buses
    people_in_buses = 10 * 27  # 10 buses, 27 people in each bus

    # Calculate the total number of people on the field trip
    total_people = people_in_vans + people_in_buses
    result = total_people
    return result

print(solution())