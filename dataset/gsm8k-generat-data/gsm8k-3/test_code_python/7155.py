def solution():
    """Pablo likes to put together jigsaw puzzles. He can put together an average of 100 pieces per hour. He has eight puzzles with 300 pieces each and five puzzles with 500 pieces each. If Pablo only works on puzzles for a maximum of 7 hours each day, how many days will it take him to complete all of his puzzles?"""
    # Define Pablo's puzzle completion rate
    PUZZLE_RATE = 100

    # Define the number of puzzles of each type
    small_puzzles = 8
    large_puzzles = 5

    # Define the number of pieces in each type of puzzle
    small_pieces = 300
    large_pieces = 500

    # Calculate the total number of puzzle pieces
    total_pieces = small_puzzles * small_pieces + large_puzzles * large_pieces

    # Calculate the total time it will take Pablo to complete all the puzzles
    total_time = total_pieces / PUZZLE_RATE

    # Calculate the number of days it will take Pablo to complete all the puzzles, given he works a maximum of 7 hours per day
    days = total_time / 7

    # Display the number of days it will take Pablo to complete all the puzzles
    result = days
    return result

print(solution())