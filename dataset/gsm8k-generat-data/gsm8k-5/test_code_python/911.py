def solution():
    time_to_nile_delta = 4  # Paul took 4 hours to walk from his home to Nile Delta
    time_return_journey = time_to_nile_delta + 2  # It took 2 more hours for Paul and six other alligators to travel from Nile Delta to their home
    total_time = time_to_nile_delta + time_return_journey  # Total time the alligators walked

    # Convert the total time into hours and minutes
    hours = total_time // 1
    minutes = int((total_time - hours) * 60)

    result = f"{hours} hours {minutes} minutes"
    return result

print(solution())