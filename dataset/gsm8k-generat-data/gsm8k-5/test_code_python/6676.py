def solution():
    # Total number of artifacts = 8 * 4 = 32 (since each wing has 4 times as many artifacts as paintings)
    # Total number of paintings = (3 * 1) + (2 * 12) = 27 (since one wing has one painting and two wings have 12 paintings each)

    # Number of wings dedicated to artifacts = 8 - 3 = 5
    # Number of artifacts per artifact wing = Total number of artifacts / Number of artifact wings
    artifacts_per_wing = 32 / 5

    result = artifacts_per_wing
    return result

print(solution())