def solution():
    
    # Define the number of slices of cheese used per sandwich and per omelet
    SANDWICH_CHEESE = 2
    OMELET_CHEESE = SANDWICH_CHEESE + 1

    # Define the number of days Carl used for breakfast and egg omelets
    breakfast_days = 3
    egg_days = 7

    # Define the number of slices of cheese used for macaroni and macaroni
    macaroni_cheese = 8

    # Calculate the total number of slices of cheese used
    total_cheese = (SANDWICH_CHEESE * 7) + (OMELET_CHEESE * breakfast_days) + (MACARONI_CHEESE * macaroni_days)

    # Display the total number of slices of cheese used
    result = total_cheese
    return result

print(solution())