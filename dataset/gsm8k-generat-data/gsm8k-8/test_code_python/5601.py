def solution():
    # Define the percentage reduction
    reduction_percentage = 25

    # Define the reduced price
    reduced_price = 6

    # Calculate the original price
    original_price = reduced_price * 100 / (100 - reduction_percentage)
    result = original_price
    return result

print(solution())