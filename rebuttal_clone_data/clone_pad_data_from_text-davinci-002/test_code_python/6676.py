def solution():
    painting_wings = 3
    painting_wing_large = 1
    painting_wing_small = 2
    painting_total = painting_wings + painting_wing_large + painting_wing_small
    artifact_wings = 8 - painting_total
    paintings = painting_wings + painting_wing_large + (painting_wing_small * 12)
    artifacts = (artifacts_wings * 4) + paintings
    result = artifacts / artifact_wings
    
    return result

print(solution())