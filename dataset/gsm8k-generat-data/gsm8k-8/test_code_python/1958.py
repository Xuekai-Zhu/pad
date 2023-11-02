def solution():
    # Define the ratio of Prejean's speed to Rickey's speed
    prejean_to_rickey_ratio = 3/4

    # Calculate the total time taken by both runners
    total_time = 70

    # Set up an equation using the ratio and total time to solve for Rickey's time
    rickey_time = total_time / (1 + prejean_to_rickey_ratio)

    result = rickey_time
    return result

print(solution())