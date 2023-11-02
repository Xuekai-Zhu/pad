def solution():
    # Calculate the number of paintings in the museum
    num_paintings = 1 + 2*12    # One painting takes up an entire wing and there are two wings with 12 smaller paintings each
    # Calculate the number of artifacts in the museum
    num_artifacts = 4*num_paintings    # The number of artifacts is four times the number of paintings
    # Calculate the number of wings dedicated to artifacts
    num_artifact_wings = 8 - 3 - 1    # Three wings are dedicated to paintings and one wing houses a single large painting
    # Calculate the number of artifacts in each artifact wing
    artifacts_per_wing = num_artifacts // num_artifact_wings
    result = artifacts_per_wing
    return result

print(solution())