def solution():
    """Nancy has six pairs of boots, nine more pairs of slippers than boots, and a number of pairs of heels equal to three times the combined number of slippers and boots. How many shoes (individual shoes, not pairs) does she have?"""
    boots_pairs = 6
    slippers_pairs = boots_pairs + 9
    combined_pairs = boots_pairs + slippers_pairs
    heels_pairs = 3 * combined_pairs

    total_shoes = 2*(boots_pairs + slippers_pairs) + heels_pairs
    result = total_shoes
    return result

print(solution())