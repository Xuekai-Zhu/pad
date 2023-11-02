def solution():
    """Rebecca drinks half a bottle of soda a day. She bought three 6-packs of sodas the last time she was at the store. How many bottles of soda will she have left after four weeks?"""
    # Define the number of bottles in a 6-pack and the number of weeks
    BOTTLES_PER_PACK = 6
    WEEKS = 4

    # Calculate the number of bottles Rebecca drinks in a week
    bottles_per_week = 0.5 * 7

    # Calculate the total number of bottles Rebecca drinks in four weeks
    total_bottles_drunk = bottles_per_week * WEEKS

    # Calculate the total number of bottles Rebecca bought
    total_bottles_bought = 3 * BOTTLES_PER_PACK

    # Calculate the total number of bottles Rebecca will have left after four weeks
    bottles_left = total_bottles_bought - total_bottles_drunk

    # Display the number of bottles Rebecca will have left
    result = bottles_left
    return result

print(solution())