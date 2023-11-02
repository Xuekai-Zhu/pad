def solution():
    # Calculate the total number of chairs produced in 6 hours by each worker
    chairs_per_worker_per_6_hours = 4 * 6

    # Calculate the total number of chairs produced by all 3 workers in 6 hours
    chairs_produced_in_6_hours = chairs_per_worker_per_6_hours * 3

    # Calculate the total number of additional chairs produced in 6 hours
    additional_chairs_produced_in_6_hours = 1

    # Calculate the total number of chairs produced in 6 hours, including the additional chairs
    total_chairs_produced_in_6_hours = chairs_produced_in_6_hours + additional_chairs_produced_in_6_hours

    result = total_chairs_produced_in_6_hours
    return result

print(solution())