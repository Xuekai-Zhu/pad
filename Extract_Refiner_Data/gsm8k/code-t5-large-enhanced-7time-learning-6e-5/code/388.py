def solution():
    
    # Define the initial cost of each service
    NETFLIX_COST = 10
    HULULY_COST = 10

    # Define the number of services Tim can get
    num_services = 1

    # Calculate the total cost of the services Tim gets
    total_cost = NETFLIX_COST * num_services

    # Calculate the cost of the Hulu and Disney Plus Plus before savings
    hulu_cost = HULULY_COST * num_services * 0.8

    # Calculate the amount Tim saves by cancelling his $60 cable package
    savings = total_cost - 60

    # Display the amount Tim saves
    result = savings
    return result

print(solution())