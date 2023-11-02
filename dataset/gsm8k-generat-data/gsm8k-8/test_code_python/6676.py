def solution():
    # Calculate the total number of paintings
    total_paintings = 1 + 12 + 12
    # Calculate the total number of artifacts
    total_artifacts = total_paintings * 4

    # Calculate the number of wings for artifacts
    artifact_wings = 8 - 3 - 1

    # Calculate the number of artifacts per wing
    artifacts_per_wing = total_artifacts / artifact_wings
    result = artifacts_per_wing
    return result

print(solution())