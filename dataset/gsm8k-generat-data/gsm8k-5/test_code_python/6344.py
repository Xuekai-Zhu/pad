def solution():
    num_jars = 5  # Daniel has 5 jars of juice
    juice_per_jar = 2 * 1000  # Each jar contains 2 liters of juice, converted to milliliters
    glass_capacity = 250  # Each glass can hold up to 250 milliliters of juice

    # Calculate the total number of glasses that can be served
    total_glasses = (num_jars * juice_per_jar) // glass_capacity  # Using integer division to round down

    result = total_glasses
    return result

print(solution())