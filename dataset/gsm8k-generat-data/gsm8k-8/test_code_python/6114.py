def solution():
    # Define the number of pairs of boots and slippers
    boots = 6
    slippers = boots + 9

    # Calculate the combined number of boots and slippers
    total_boots_slippers = boots + slippers

    # Calculate the number of pairs of heels
    heels = 3 * total_boots_slippers

    # Calculate the total number of shoes
    total_shoes = 2 * (boots + slippers + heels)
    result = total_shoes
    return result

print(solution())