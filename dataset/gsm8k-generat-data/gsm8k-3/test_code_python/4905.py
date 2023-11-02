def solution():
    """Hilary is collecting her toenails in a jar to gross out her sister. She can fit 100 toenails in the jar, unless they are from her two big toes, which are twice as big as the rest. She has already filled it with 20 big toenails and 40 regular toenails. How many regular toenails can she fit into the remainder of the jar?"""
    # Define the capacity of the jar
    JAR_CAPACITY = 100

    # Define the space taken up by Hilary's big toenails
    BIG_TOENAIL_SPACE = 4

    # Calculate the space taken up by Hilary's regular toenails
    regular_toenail_space = (JAR_CAPACITY - BIG_TOENAIL_SPACE) / 2

    # Calculate the space remaining in the jar after filling it with Hilary's toenails
    remaining_space = JAR_CAPACITY - 20 - BIG_TOENAIL_SPACE - regular_toenail_space

    # Calculate the maximum number of regular toenails that can fit in the remaining space
    max_regular_toenails = remaining_space / 1

    # Display the maximum number of regular toenails that can fit in the remaining space
    result = max_regular_toenails
    return result

print(solution())