def solution():
    """Owen bred 21 turtles, and Johanna has 5 fewer turtles than Owen. After 1 month, Owen has twice as many turtles as before and Johanna loses half of her turtles and donates the rest to Owen. How many turtles did Owen have?"""
    # Define the initial number of turtles Owen had
    owen_turtles = 21

    # Calculate the number of turtles Johanna had
    johanna_turtles = owen_turtles - 5

    # Calculate the number of turtles Owen had after 1 month
    owen_turtles_after_month = owen_turtles * 2

    # Calculate the number of turtles Johanna had after 1 month
    johanna_turtles_after_month = johanna_turtles // 2

    # Calculate the total number of turtles Owen had after receiving Johanna's turtles
    total_turtles = owen_turtles_after_month + johanna_turtles_after_month

    # Display the total number of turtles Owen had
    result = total_turtles
    return result

print(solution())