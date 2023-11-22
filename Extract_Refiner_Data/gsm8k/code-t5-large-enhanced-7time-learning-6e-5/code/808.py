def solution():
    
    # Define the number of flowers picked by each person
    initial_flowers = [3, 5, 6, 4, 5, 6, 7]
    final_flowers = [6, 7, 7]

    # Calculate the total number of petals picked
    total_petals = sum(initial_flowers)

    # Subtract the petals picked by the first three flowers
    remaining_petals = total_petals - sum(initial_flowers)

    # Subtract the petals picked by the last three flowers
    remaining_petals -= 1

    # Display the number of remaining flowers
    result = remaining_petals
    return result

print(solution())