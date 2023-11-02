def solution():
    """There are 50 oysters on the rocks at La Push Park and 72 crabs by the beach. Eric, who loves walking by the beach, makes a note of this and goes home. The next day, he realizes only half the number of Oysters were on the rocks, and only 2/3 the number of crabs as the previous day are on the beach. How many oysters and crabs did he count in total in the two days?"""
    day_1_oysters = 50
    day_1_crabs = 72
    day_2_oysters = day_1_oysters / 2
    day_2_crabs = day_1_crabs * (2/3)
    total_oysters = day_1_oysters + day_2_oysters
    total_crabs = day_1_crabs + day_2_crabs
    result = total_oysters + total_crabs
    return result

print(solution())