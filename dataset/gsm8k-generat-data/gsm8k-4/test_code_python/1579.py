def solution():
    """Last night, Olive charged her phone for 10 hours. Assuming each hour of charge lasts the phone 2 hours of use, calculate the total time Olive would be able to use her phone before it goes off if she charges it for 3/5 of the time she charged the phone last night."""
    # Define the total hours Olive charged her phone
    total_hours = 10

    # Calculate the hours of use per hour of charge
    hours_per_charge = 2

    # Calculate the hours Olive charged her phone for if she charged for 3/5 of the time
    new_hours = total_hours * 3/5

    # Calculate the total hours of use
    total_use_hours = new_hours * hours_per_charge

    result = total_use_hours
    return result

print(solution())