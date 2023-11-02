def solution():
    """Naomi is doing the wash. First she makes piles of different types, with one pile for towels, one for sheets, and one for clothes that need to be washed on the gentle cycle. The clothes take 30 minutes to wash. The towels take twice as long as the clothes to wash. The sheets take 15 minutes less time to wash than the towels. How many minutes total will it take for Naomi to wash everything?"""
    # Define the time to wash clothes and calculate the time to wash towels and sheets
    clothes_time = 30
    towels_time = clothes_time * 2
    sheets_time = towels_time - 15

    # Calculate the total time to wash everything
    total_time = clothes_time + towels_time + sheets_time

    result = total_time
    return result

print(solution())