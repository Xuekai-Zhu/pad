def solution():
    """Pablo likes to put together jigsaw puzzles. He can put together an average of 100 pieces per hour. He has eight puzzles with 300 pieces each and five puzzles with 500 pieces each. If Pablo only works on puzzles for a maximum of 7 hours each day, how many days will it take him to complete all of his puzzles?"""
    pieces_per_hour = 100
    max_hours_per_day = 7
    total_pieces = 8 * 300 + 5 * 500
    total_hours = total_pieces / pieces_per_hour
    total_days = total_hours / max_hours_per_day
    result = total_days
    return result

print(solution())