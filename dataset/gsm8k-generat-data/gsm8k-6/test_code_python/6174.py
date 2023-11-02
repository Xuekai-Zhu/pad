def solution():
    # Calculate the total cups of flour used in 3 batches of cookies
    total_flour_used = 2 * 3  # recipe for 1 batch of cookies calls for 2 cups of flour and she bakes 3 batches

    # Calculate the cups of flour remaining after baking 3 batches
    remaining_flour = 20 - total_flour_used

    # Calculate the number of batches of cookies she could make with the remaining flour
    remaining_batches = remaining_flour // 2

    result = remaining_batches
    return result

print(solution())