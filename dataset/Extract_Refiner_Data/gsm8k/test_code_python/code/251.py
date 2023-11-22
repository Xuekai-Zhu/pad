def solution():
    
    # Define the initial number of cows per stall and the number of stalls
    INITIAL_COWS_PER_STALL = 20
    NUM_STALLS = 10

    # Define the number of cows purchased and the number of stalls purchased
    COWS_PURCHASED = 40
    NUM_STALLS_PURCHASED = 20

    # Calculate the total number of cows purchased
    total_cows_purchased = COWS_PURCHASED / NUM_STALLS_PURCHASED

    # Calculate the number of new cows in each stall after dividing the purchases equally
    new_cows_per_stall = INITIAL_COWS_PER_STALL / NUM_STALLS_PURCHASED

    # Calculate the total number of new cows in 8 stalls
    total_new_cows = new_cows_per_stall * NUM_STALLS_PURCHASE

print(solution())