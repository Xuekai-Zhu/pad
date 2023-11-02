def solution():
    """A museum has eight different wings displaying four times as many artifacts as paintings displayed. Three of the wings are dedicated to paintings. The artifacts are divided evenly among the remaining wings. One painting is so large it takes up an entire wing, and the other two wings house 12 smaller paintings each. How many artifacts are in each artifact wing?"""
    # Define the number of paintings in the museum
    paintings = 1 + 2 + 12 + 12

    # Calculate the number of artifacts
    artifacts = 4 * paintings

    # Calculate the number of wings dedicated to artifacts
    artifact_wings = 8 - 3 - 1

    # Calculate the number of artifacts in each artifact wing
    artifacts_per_wing = artifacts / artifact_wings

    result = artifacts_per_wing
    return result

print(solution())