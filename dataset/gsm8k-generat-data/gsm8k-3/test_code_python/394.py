def solution():
    """Naomi is doing the wash. First she makes piles of different types, with one pile for towels, one for sheets, and one for clothes that need to be washed on the gentle cycle. The clothes take 30 minutes to wash. The towels take twice as long as the clothes to wash. The sheets take 15 minutes less time to wash than the towels. How many minutes total will it take for Naomi to wash everything?"""
    # Define the time it takes to wash clothes, towels, and sheets
    CLOTHES_TIME = 30
    TOWELS_TIME = CLOTHES_TIME * 2
    SHEETS_TIME = TOWELS_TIME - 15

    # Calculate the total time it will take to wash everything
    total_time = CLOTHES_TIME + TOWELS_TIME + SHEETS_TIME

    # Display the total time
    result = total_time
    return result

print(solution())