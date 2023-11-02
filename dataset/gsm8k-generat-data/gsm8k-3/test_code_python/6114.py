def solution():
    """Nancy has six pairs of boots, nine more pairs of slippers than boots, and a number of pairs of heels equal to three times the combined number of slippers and boots. How many shoes (individual shoes, not pairs) does she have?"""
    # Define the number of pairs for each type of shoe
    boots_pairs = 6
    slippers_pairs = boots_pairs + 9
    heels_pairs = 3 * (boots_pairs + slippers_pairs)

    # Calculate the total number of individual shoes
    total_shoes = (boots_pairs * 2) + (slippers_pairs * 2) + (heels_pairs * 2)

    # Display the total number of shoes
    result = total_shoes
    return result

print(solution())