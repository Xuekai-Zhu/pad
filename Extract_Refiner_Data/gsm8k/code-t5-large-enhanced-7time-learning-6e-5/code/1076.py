def solution():
    
    # Define the rate of creating a new jellyfish
    rate = 1 / 60  # 1/2 of an hour

    # Calculate the number of jellyfish created in 4 hours
    jellyfish_creation = rate * 4

    # Calculate the total number of jellyfish created
    total_jellyfish = jellyfish_creation * 5

    # Display the total number of jellyfish created
    result = total_jellyfish
    return result

print(solution())