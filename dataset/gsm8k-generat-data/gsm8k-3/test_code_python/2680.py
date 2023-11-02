def solution():
    """James decides to try and collect rare artifacts in the field.  He spends 6 months researching before going on a 2-year-long expedition for his first find.  The second artifact takes 3 times as long for the research and discovery.  How long did it take him to find both?"""
    # Define the time it takes for research and discovery of the first artifact
    first_artifact_time = 6 + 24  # 6 months of research + 2 years of expedition

    # Define the time it takes for research and discovery of the second artifact
    second_artifact_time = 3 * first_artifact_time

    # Calculate the total time it takes to find both artifacts
    total_time = first_artifact_time + second_artifact_time

    # Display the total time
    result = total_time
    return result

print(solution())