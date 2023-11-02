def solution():
    # Calculate the number of pairs of slippers
    boots_pairs = 6
    slippers_pairs = boots_pairs + 9

    # Calculate the combined number of boots and slippers pairs
    combined_pairs = boots_pairs + slippers_pairs

    # Calculate the number of pairs of Heels
    heels_pairs = combined_pairs * 3

    # Calculate the total number of shoes
    total_shoes = (boots_pairs + slippers_pairs + heels_pairs) * 2  # Multiply by 2 to get the number of individual shoes

    result = total_shoes
    return result

print(solution())