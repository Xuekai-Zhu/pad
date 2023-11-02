def solution():
    charge_time = 10  # Olive charged her phone for 10 hours
    phone_use_time = 2  # Each hour of charge lasts the phone 2 hours of use
    partial_charge_time = (3/5) * charge_time  # Olive charges her phone for 3/5 of the time she charged it last night

    # Calculate the total time Olive would be able to use her phone
    total_use_time = phone_use_time * partial_charge_time

    result = total_use_time
    return result

print(solution())