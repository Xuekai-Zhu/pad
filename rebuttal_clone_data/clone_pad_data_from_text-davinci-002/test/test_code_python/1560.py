def solution():
    total_stems = 52
    stems_given_to_mom = 15
    stems_given_to_grandma = stems_given_to_mom + 6
    stems_in_vase = total_stems - stems_given_to_mom - stems_given_to_grandma
    result = stems_in_vase
    return result

print(solution())