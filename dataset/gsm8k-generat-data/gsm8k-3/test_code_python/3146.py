def solution():
    """George and Harry want to fill a pool with buckets. George can carry two buckets each round, and Harry can carry three buckets each round. If it takes 110 buckets to fill the pool, how many rounds will it take to fill the pool?"""
    # Define the number of buckets George and Harry can carry each round
    GEORGE_BUCKET = 2
    HARRY_BUCKET = 3

    # Define the total number of buckets needed to fill the pool
    TOTAL_BUCKETS = 110

    # Calculate the total number of rounds needed to fill the pool
    total_rounds = TOTAL_BUCKETS // (GEORGE_BUCKET + HARRY_BUCKET)

    # Display the total number of rounds needed
    result = total_rounds
    return result

print(solution())