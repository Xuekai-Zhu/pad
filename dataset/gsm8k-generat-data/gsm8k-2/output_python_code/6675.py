def solution():
    """A museum has eight different wings displaying four times as many artifacts as paintings displayed. Three of the wings are dedicated to paintings. The artifacts are divided evenly among the remaining wings. One painting is so large it takes up an entire wing, and the other two wings house 12 smaller paintings each. How many artifacts are in each artifact wing?"""
    num_paintings = (1*1) + (2*12)
    num_artifacts = num_paintings * 4
    num_artifact_wings = 8 - 3 - 1 - 2
    artifacts_per_wing = num_artifacts / num_artifact_wings
    result = artifacts_per_wing
    return result

print(solution())