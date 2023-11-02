def solution():
    """Jane, Kyla, and Anthony have summer jobs in a resort. Their task is to fold guests' towels. Jane can fold 3 towels in 5 minutes. Kyla can fold 5 towels in 10 minutes, and Anthony can fold 7 towels in 20 minutes. If they all fold towels together, how many towels can they fold in one hour?"""
    # Convert the times to towels per minute
    jane_tpm = 3 / 5
    kyla_tpm = 5 / 10
    anthony_tpm = 7 / 20

    # Calculate the combined towels per minute of all three workers
    combined_tpm = jane_tpm + kyla_tpm + anthony_tpm

    # Convert the combined towels per minute to towels per hour
    tph = combined_tpm * 60 * 60

    # return the result
    result = round(tph)
    return result

print(solution())