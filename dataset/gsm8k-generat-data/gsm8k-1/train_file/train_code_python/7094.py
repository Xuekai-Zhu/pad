def solution():
    """There are 50 oysters on the rocks at La Push Park and 72 crabs by the beach. Eric, who loves walking by the beach, makes a note of this and goes home. The next day, he realizes only half the number of Oysters were on the rocks, and only 2/3 the number of crabs as the previous day are on the beach. How many oysters and crabs did he count in total in the two days?"""
    initial_oysters = 50
    initial_crabs = 72
    second_day_oysters = initial_oysters / 2
    second_day_crabs = initial_crabs * (2 / 3)
    total_oysters = initial_oysters + second_day_oysters
    total_crabs = initial_crabs + second_day_crabs
    result = total_oysters + total_crabs
    
    return result

print(solution())