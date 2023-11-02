def solution():
    # Define the number of hard hats in the truck
    pink_hats = 26
    green_hats = 15
    yellow_hats = 24

    # Remove some hard hats
    pink_hats -= 4
    green_hats -= 6
    green_hats -= 2 * 4

    # Calculate the total number of hard hats
    total_hats = pink_hats + green_hats + yellow_hats
    result = total_hats
    return result

print(solution())