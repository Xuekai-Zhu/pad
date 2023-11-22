def solution():
    
    # Define the number of signatures collected by Carol and Jennifer
    carol_signatures = 20
    jennifer_signatures = 44

    # Calculate the total number of signatures collected after five weeks
    total_signatures = carol_signatures + jennifer_signatures

    # Calculate the number of weeks it took to reach 100 signatures
    weeks_to_reach_100_signatures = 3
    total_weeks = 5
    weeks_to_reach_100_signatures = weeks_to_reach_100_signatures * total_weeks

    # Calculate the number of signatures remaining after the vacation
    remaining_signatures = total_signatures - total_weeks

    # Return the result
    result = remaining_signatures
    return result

print(solution())