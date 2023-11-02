def solution():
    """Last night, Olive charged her phone for 10 hours. Assuming each hour of charge lasts the phone 2 hours of use, calculate the total time Olive would be able to use her phone before it goes off if she charges it for 3/5 of the time she charged the phone last night."""
    # Define the number of hours Olive charged her phone
    total_charge_hours = 10

    # Calculate the number of hours Olive charged her phone for this time
    partial_charge_hours = total_charge_hours * 3 / 5

    # Calculate the total number of hours Olive can use her phone
    total_use_hours = partial_charge_hours * 2

    # Display the total number of hours Olive can use her phone
    result = total_use_hours
    return result

print(solution())