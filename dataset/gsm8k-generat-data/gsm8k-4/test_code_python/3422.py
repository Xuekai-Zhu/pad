def solution():
    """James buys 2 puzzles that are 2000 pieces each. He anticipates for these larger puzzles he can do 100 pieces every 10 minutes. So how long would it take to finish both puzzles?"""
    
    # Define the number of pieces per puzzle and the puzzle completion rate 
    PIECES_PER_PUZZLE = 2000
    COMPLETION_RATE = 10/100
    
    # Calculate the total number of pieces to complete both puzzles
    total_pieces = PIECES_PER_PUZZLE * 2
    
    # Calculate the total time required to complete both puzzles
    total_time = (total_pieces / 100) * COMPLETION_RATE
    
    # return the result
    result = total_time
    return result

print(solution())