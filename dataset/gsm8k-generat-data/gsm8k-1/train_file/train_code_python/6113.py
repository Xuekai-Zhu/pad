def solution():
    """Nancy has six pairs of boots, nine more pairs of slippers than boots, and a number of pairs of heels equal to three times the combined number of slippers and boots. How many shoes (individual shoes, not pairs) does she have?"""
    boots = 6 * 2 # since each pair has 2 shoes
    slippers = (6 + 9) * 2 # since she has 9 more pairs of slippers than boots
    heels = (6 + 9) * 3 * 2 # since the number of pairs of heels is equal to three times the combined number of slippers and boots, and each pair has 2 shoes
    total_shoes = boots + slippers + heels
    result = total_shoes
    return result

print(solution())