def solution():
    """Hilary is collecting her toenails in a jar to gross out her sister. She can fit 100 toenails in the jar, unless they are from her two big toes, which are twice as big as the rest. She has already filled it with 20 big toenails and 40 regular toenails. How many regular toenails can she fit into the remainder of the jar?"""
    # Define the capacity of the jar
    JAR_CAPACITY = 100

    # Define the number of big toenails already in the jar
    big_toenails = 20 + (2 * 2)

    # Define the number of regular toenails already in the jar
    regular_toenails = 40

    # Calculate the remaining capacity of the jar for regular toenails
    remaining_capacity = JAR_CAPACITY - big_toenails - regular_toenails

    result = remaining_capacity 
    return result

print(solution())