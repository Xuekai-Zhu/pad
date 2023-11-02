def solution():
    # Define the number of loads of laundry washed on each day
    wednesday = 6
    thursday = 2 * wednesday
    friday = thursday / 2
    saturday = wednesday / 3

    # Calculate the total number of loads of laundry washed
    total_laundry = wednesday + thursday + friday + saturday
    result = total_laundry
    return result

print(solution())