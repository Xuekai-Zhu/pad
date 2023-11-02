def solution():
    """A jar of jellybeans has 14 blue jellybeans, 26 purple jellybeans and 40 orange jellybeans. If there are 200 jellybeans in the jar, how many are there of the red color?"""
    # Define the number of each color of jellybeans
    blue_jellybeans = 14
    purple_jellybeans = 26
    orange_jellybeans = 40

    # Calculate the total number of jellybeans
    total_jellybeans = blue_jellybeans + purple_jellybeans + orange_jellybeans

    # Calculate the number of red jellybeans
    red_jellybeans = 200 - total_jellybeans

    # Display the number of red jellybeans
    result = red_jellybeans
    return result

print(solution())