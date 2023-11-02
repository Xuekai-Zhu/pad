def solution():
    """Last night, Olive charged her phone for 10 hours. Assuming each hour of charge lasts the phone 2 hours of use, calculate the total time Olive would be able to use her phone before it goes off if she charges it for 3/5 of the time she charged the phone last night."""
    charge_time = 10
    use_time_per_charge = 2
    partial_charge_time = 3/5 * charge_time
    total_use_time = use_time_per_charge * partial_charge_time
    result = total_use_time
    return result

print(solution())