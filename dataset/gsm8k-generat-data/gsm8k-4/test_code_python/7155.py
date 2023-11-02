def solution():
    """Pablo likes to put together jigsaw puzzles. He can put together an average of 100 pieces per hour. He has eight puzzles with 300 pieces each and five puzzles with 500 pieces each. If Pablo only works on puzzles for a maximum of 7 hours each day, how many days will it take him to complete all of his puzzles?"""
    # Define the average number of pieces Pablo can put together per hour
    pieces_per_hour = 100

    # Define the number of puzzles Pablo has
    puzzles = [300] * 8 + [500] * 5

    # Define the total number of pieces Pablo has to assemble
    total_pieces = sum(puzzles)

    # Define the total number of hours Pablo can work each day
    daily_hours = 7

    # Calculate the total number of days it will take for Pablo to complete all of his puzzles
    total_hours = total_pieces / pieces_per_hour
    total_days = total_hours / daily_hours

    # Return the result
    result = round(total_days)
    return result

print(solution())