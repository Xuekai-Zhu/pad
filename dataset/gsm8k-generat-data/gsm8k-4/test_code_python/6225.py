def solution():
    """Pedro, Linden, and Jesus are playing a game. Jesus has 60 squares. Linden has 75 squares. Pedro has 200. How many more squares does Pedro have than both Jesus and Linden combined?"""
    
    # Define the number of squares for Jesus, Linden and Pedro
    jesus_squares = 60
    linden_squares = 75
    pedro_squares = 200

    # Calculate the combined number of squares for Jesus and Linden
    combined_squares = jesus_squares + linden_squares

    # Calculate the difference between Pedro's squares and the combined squares of Jesus and Linden
    difference = pedro_squares - combined_squares

    # return the result
    result = difference
    return result

print(solution())