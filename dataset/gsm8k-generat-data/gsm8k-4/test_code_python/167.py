def solution():
    """Janet filmed a new movie that is 60% longer than her previous 2-hour long movie. Her previous movie cost $50 per minute to film, and the newest movie cost twice as much per minute to film as the previous movie. What was the total amount of money required to film Janet's entire newest film?"""
    # Define the length of the previous movie in minutes
    previous_length = 120

    # Calculate the length of the new movie in minutes
    new_length = previous_length * 1.6

    # Calculate the cost per minute of filming the previous movie
    previous_cost = 50

    # Calculate the cost per minute of filming the new movie
    new_cost = previous_cost * 2

    # Calculate the total cost of filming the new movie
    total_cost = new_length * new_cost

    # Return the result
    result = total_cost
    return result

print(solution())