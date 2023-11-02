def solution():
    # Calculate the total time the phone can be used if charged for 10 hours
    total_use_time = 10 * 2

    # Calculate the time Olive charges her phone for tonight
    tonight_charge_time = 3/5 * 10

    # Calculate the total use time based on tonight's charge time
    tonight_use_time = tonight_charge_time * 2

    # Calculate the updated total use time
    updated_use_time = total_use_time + tonight_use_time

    result = updated_use_time
    return result

print(solution())