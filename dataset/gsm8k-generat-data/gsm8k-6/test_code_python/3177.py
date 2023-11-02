def solution():
    # Calculate the total number of loads of laundry Vincent washed during the week
    wednesday_loads = 6
    thursday_loads = 2 * wednesday_loads
    friday_loads = thursday_loads / 2
    saturday_loads = wednesday_loads / 3

    total_loads = wednesday_loads + thursday_loads + friday_loads + saturday_loads
    result = total_loads
    return result

print(solution())