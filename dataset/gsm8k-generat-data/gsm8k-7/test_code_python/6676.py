def solution():
    num_paintings = 27  # 1 large painting + 2 wings with 12 paintings each
    num_artifact_wings = 8 - 3  # 8 wings in total, minus 3 wings for paintings
    paintings_per_wing = 1  # 1 wing for a large painting, 2 wings for 12 smaller paintings each

    # Calculate the total number of paintings displayed
    total_paintings = num_paintings + (paintings_per_wing * num_paintings)

    # Calculate the total number of artifacts displayed
    total_artifacts = total_paintings * 4

    # Calculate the number of artifacts in each artifact wing
    artifacts_per_wing = total_artifacts / num_artifact_wings
    result = artifacts_per_wing
    return result

print(solution())