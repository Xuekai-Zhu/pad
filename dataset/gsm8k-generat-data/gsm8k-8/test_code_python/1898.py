def solution():
    # Calculate the total number of hushpuppies needed
    total_hushpuppies = 5 * 20

    # Calculate the number of batches needed
    batches = total_hushpuppies / 10

    # Calculate the total cooking time for all batches
    total_cooking_time = batches * 8

    result = total_cooking_time
    return result

print(solution())