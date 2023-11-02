def solution():
    """Susan is playing a board game with 48 spaces from the starting space to the winning end space of the game. On the first turn, she moves forward eight spaces. On the second turn, she moves two spaces, but lands on a space that sends her back five spaces. On the third turn, she moves forward six more spaces. How many spaces does she have to move to reach the ending space and win the game?"""
    
    # Initialize Susan's position on the board
    position = 8
    
    # Move forward 2 spaces on the second turn, then back 5 spaces
    position += 2
    position -= 5
    
    # Move forward 6 more spaces on the third turn
    position += 6
    
    # Calculate how many spaces Susan has left to move to reach the end of the game
    spaces_left = 48 - position
    
    # Display the number of spaces left to move
    result = spaces_left
    return result

print(solution())