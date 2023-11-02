def solution():
    research_time = 6 # in months
    first_artifact_expedition_time = 2 # in years
    second_artifact_expedition_time = first_artifact_expedition_time * 3 # in years

    # Convert all time to years
    research_time = research_time / 12
    first_artifact_expedition_time = first_artifact_expedition_time
    second_artifact_expedition_time = second_artifact_expedition_time

    # Calculate the total time it took James to find both artifacts
    total_time = research_time + first_artifact_expedition_time + second_artifact_expedition_time
    result = total_time
    return result

print(solution())