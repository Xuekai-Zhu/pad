def solution():
    total_apples = 200
    rotten_percentage = 0.4
    rotten_apples = total_apples * rotten_percentage
    smelling_rotten_percentage = 0.7
    smelling_rotten_apples = rotten_apples * smelling_rotten_percentage
    not_smelling_rotten_apples = rotten_apples - smelling_rotten_apples
    result = not_smelling_rotten_apples
    return result

print(solution())