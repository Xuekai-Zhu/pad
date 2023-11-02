def solution():
    """There are three buckets of seeds labeled A, B, and C with 100 seeds. There are ten more seeds in bucket A than in bucket B, and bucket B has 30 seeds. How many seeds are in bucket C?"""
    # Define the number of seeds in bucket B
    B = 30

    # Calculate the number of seeds in bucket A using the information given
    A = B + 10

    # Calculate the total number of seeds in buckets A and B
    total_AB = A + B

    # Calculate the number of seeds in bucket C by subtracting the total number of seeds in buckets A and B from the total number of seeds (100)
    C = 100 - total_AB

    # Display the number of seeds in bucket C
    result = C
    return result

print(solution())