def solution():
    
    # Define the time it takes for each task
    swim_time = 40
    bike_time = 20
    run_time = 50

    # Calculate the time it takes for James to finish the swim
    swim_time_after_work = swim_time * 1.1
    swim_time_after_work = swim_time_after_work + 5

    # Calculate the total time it takes for James to finish the run
    run_time_after_work = run_time + swim_time_after_work

    # Calculate the time it takes for James to finish the run
    james_time_after_work = run_time_after_work - 10

    # Display the time it takes for James to finish the run
    result = james_time_after_work
    return result

print(solution())