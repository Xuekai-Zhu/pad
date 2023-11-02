def solution():
    """James decides to try and collect rare artifacts in the field.  He spends 6 months researching before going on a 2-year-long expedition for his first find. The second artifact takes 3 times as long for the research and discovery. How long did it take him to find both?"""
    # Define the time spent researching and the time spent on the first expedition
    research_time = 6/12  # Convert 6 months to years
    expedition1_time = 2

    # Define the time spent on the second artifact, which is three times as long as the first one
    expedition2_time = 3 * expedition1_time

    # Calculate the total time spent on both artifacts
    total_time = research_time + expedition1_time + expedition2_time

    # Return the total time in years
    result = total_time
    return result

print(solution())