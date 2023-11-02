def solution():
    """Pedro, Linden, and Jesus are playing a game. Jesus has 60 squares. Linden has 75 squares. Pedro has 200. How many more squares does Pedro have than both Jesus and Linden combined?"""
    jesus_squares = 60
    linden_squares = 75
    pedro_squares = 200
    total_squares = jesus_squares + linden_squares
    diff_squares = pedro_squares - total_squares
    result = diff_squares
    return result

print(solution())