def solution():
    """There were 90 jellybeans in a jar. Samantha snuck 24 jellybeans out of the jar, without being seen. Shelby ate 12 jellybeans from the jar. Their mom, Shannon, refilled the jar with half as much as Samantha and Shelby took out. How many jellybeans are in the jar now?"""
    # Define the initial number of jellybeans in the jar
    initial_jellybeans = 90

    # Calculate the number of jellybeans left after Samantha takes out 24
    jellybeans_left = initial_jellybeans - 24

    # Calculate the number of jellybeans left after Shelby eats 12
    jellybeans_left -= 12

    # Calculate the amount of jellybeans Shannon refilled the jar with
    refill_amount = (24 + 12) / 2

    # Calculate the final number of jellybeans in the jar
    final_jellybeans = jellybeans_left + refill_amount

    # Display the final number of jellybeans in the jar
    result = final_jellybeans
    return result

print(solution())