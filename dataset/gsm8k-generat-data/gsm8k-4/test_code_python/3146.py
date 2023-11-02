def solution():
    """George and Harry want to fill a pool with buckets. George can carry two buckets each round, and Harry can carry three buckets each round. If it takes 110 buckets to fill the pool, how many rounds will it take to fill the pool?"""
    # Define the number of buckets carried by George and Harry per round
    GEORGE_BUCKETS_PER_ROUND = 2
    HARRY_BUCKETS_PER_ROUND = 3

    # Define the total number of buckets needed to fill the pool
    TOTAL_BUCKETS = 110

    # Calculate the total number of rounds needed to fill the pool
    total_rounds = 0
    while TOTAL_BUCKETS > 0:
        # George and Harry carry their buckets
        TOTAL_BUCKETS -= GEORGE_BUCKETS_PER_ROUND + HARRY_BUCKETS_PER_ROUND
        # Increment the round counter
        total_rounds += 1

    # Return the number of rounds needed
    result = total_rounds
    return result

print(solution())