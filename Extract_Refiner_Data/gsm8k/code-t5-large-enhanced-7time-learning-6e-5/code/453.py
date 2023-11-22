def solution():
    
    # Define the number of fairies seen above the forest
    initial_fairies = 50

    # Calculate the number of fairies seen after 20 minutes
    fairies_after_20min = initial_fairies / 2

    # Calculate the number of fairies seen after 10 minutes
    fairies_after_10min = fairies_after_20min + 30

    # Calculate the number of fairies remaining
    fairies_remaining = fairies_after_10min - initial_fairies

    # Display the number of fairies remaining
    result = fairies_remaining
    return result

print(solution())