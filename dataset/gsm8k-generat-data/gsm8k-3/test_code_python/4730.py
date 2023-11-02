def solution():
    """There are twice as many cows as dogs at a petting farm. If there are currently 184 cows at the farm, and the farm owner decides to sell 1/4 of the cows and 3/4 of the dogs, how many animals are remaining on the farm?"""
    # Define the number of cows and dogs at the petting farm
    cow_count = 184
    dog_count = cow_count // 2

    # Calculate the number of cows and dogs sold
    cows_sold = cow_count // 4
    dogs_sold = dog_count * 3 // 4

    # Calculate the number of cows and dogs remaining
    cows_remaining = cow_count - cows_sold
    dogs_remaining = dog_count - dogs_sold

    # Calculate the total number of animals remaining
    total_remaining = cows_remaining + dogs_remaining

    # Display the total number of animals remaining
    result = total_remaining
    return result

print(solution())