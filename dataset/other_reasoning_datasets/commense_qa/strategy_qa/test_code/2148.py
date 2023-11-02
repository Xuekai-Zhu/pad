def solution():
    oil_spill_pollution = True
    job_loss_due_to_pollution = True
    fossil_fuel_use_in_the_Gulf_of_Mexico = True
    if oil_spill_pollution and job_loss_due_to_pollution and fossil_fuel_use_in_the_Gulf_of_Mexico:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())