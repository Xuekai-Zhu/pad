def solution():
    """Pedro, Linden, and Jesus are playing a game. Jesus has 60 squares. Linden has 75 squares. Pedro has 200. How many more squares does Pedro have than both Jesus and Linden combined?"""
    # Define the number of squares for each player
    jesus_squares = 60
    linden_squares = 75
    pedro_squares = 200

    # Calculate the total number of squares for Jesus and Linden combined
    combined_squares = jesus_squares + linden_squares

    # Calculate the number of squares Pedro has more than Jesus and Linden combined
    difference = pedro_squares - combined_squares

    # Display the result
    result = difference
    return result

print(solution())