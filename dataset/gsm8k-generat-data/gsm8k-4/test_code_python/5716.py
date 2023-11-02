def solution():
    """2 tablespoons of popcorn kernels will make 4 cups of popcorn.
    For movie night, Joanie wants 3 cups of popcorn, Mitchell wants 4 cups of popcorn,
    Miles and Davis said they would split 6 cups of popcorn and Cliff said he would only eat 3 cups.
    How many tablespoons of popcorn kernels will they need?"""
    
    # Calculate the total number of cups of popcorn needed
    total_cups = 3 + 4 + 6 + 3

    # Calculate the total number of tablespoons needed
    total_tablespoons = (total_cups / 4) * 2

    # Return the result
    result = total_tablespoons
    return result

print(solution())