def solution():
    
    # Define the number of bottles produced by each juice per day
    bottles_per_day = 4200

    # Define the daily energy requirement of each juice
    daily_requirement = 0.2 * bottles_per_day

    # Calculate the total number of people who need to be satisfied
    total_people = 2300

    # Calculate the number of bottles of juices that can be produced in the given time period
    total_juices = total_people * daily_requirement

    # Calculate the number of bottles of juices that Hortex needs to produce to meet 100% of the daily energy requirement
    additional_juices = total_juices * (1 - daily_requirement)

    # Display the number of additional bottles of juices Hortex needs to produce
    result = additional_juices
    return result

print(solution())