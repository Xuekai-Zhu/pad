def solution():
    """2 tablespoons of popcorn kernels will make 4 cups of popcorn.  For movie night, Joanie wants 3 cups of popcorn, Mitchell wants 4 cups of popcorn, Miles and Davis said they would split 6 cups of popcorn and Cliff said he would only eat 3 cups.  How many tablespoons of popcorn kernels will they need?"""
    # Define the conversion factor
    CONVERSION_FACTOR = 2/4 # 2 tablespoons makes 4 cups

    # Calculate the total amount of popcorn needed
    total_popcorn = 3 + 4 + 6 + 3

    # Calculate the amount of popcorn kernels needed
    popcorn_kernels = total_popcorn / CONVERSION_FACTOR

    # Display the amount of popcorn kernels needed
    result = popcorn_kernels
    return result

print(solution())