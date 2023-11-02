def solution():
    """There were 37 jellybeans in a jar. Pat removed 15 of them. Pat then added 5 of the removed jellybeans back in, and then removed 4 more. How many jellybeans are now in the jar?"""
    # Define the number of jellybeans in the jar initially
    initial_jellybeans = 37

    # Calculate the number of jellybeans after Pat removes 15
    jellybeans_after_removal = initial_jellybeans - 15

    # Calculate the number of jellybeans after Pat adds 5 back in
    jellybeans_after_addition = jellybeans_after_removal + 5

    # Calculate the final number of jellybeans after Pat removes 4 more
    final_jellybeans = jellybeans_after_addition - 4

    # Display the final number of jellybeans in the jar
    result = final_jellybeans
    return result

print(solution())