def solution():
    """Owen bred 21 turtles, and Johanna has 5 fewer turtles than Owen. After 1 month, Owen has twice as many turtles as before and Johanna loses half of her turtles and donates the rest to Owen. How many turtles did Owen have?"""
    # Define the initial number of turtles bred by Owen
    owen_turtles = 21

    # Define the number of turtles Johanna has
    johanna_turtles = owen_turtles - 5

    # Calculate the number of turtles Owen has after 1 month
    owen_turtles_after_1_month = owen_turtles * 2

    # Calculate the number of turtles Johanna has after losing half and donating the rest to Owen
    johanna_turtles_after_1_month = johanna_turtles // 2
    owen_turtles_after_donation = owen_turtles_after_1_month + johanna_turtles_after_1_month

    # Return the number of turtles Owen had initially
    result = owen_turtles_after_donation
    return result

print(solution())