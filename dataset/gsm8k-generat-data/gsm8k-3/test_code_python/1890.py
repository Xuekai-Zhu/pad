def solution():
    """Jane, Kyla, and Anthony have summer jobs in a resort. Their task is to fold guests' towels. Jane can fold 3 towels in 5 minutes. Kyla can fold 5 towels in 10 minutes, and Anthony can fold 7 towels in 20 minutes. If they all fold towels together, how many towels can they fold in one hour?"""
    # Define the number of towels each person can fold in 1 minute
    JANE_RATE = 0.6
    KYLA_RATE = 0.5
    ANTHONY_RATE = 0.35

    # Calculate the combined rate of all three people
    combined_rate = JANE_RATE + KYLA_RATE + ANTHONY_RATE

    # Calculate the total number of towels they can fold in 1 hour
    towels_per_hour = combined_rate * 60

    # Display the total number of towels
    result = towels_per_hour
    return result

print(solution())