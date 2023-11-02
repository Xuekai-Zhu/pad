def solution():
    """
    A hay farmer harvested 560 bales of hay from 5 acres of grass per month last year. This year, he planted an additional 7 acres of grass. If the farmer also owns 9 horses and each horse consumes 3 bales of hay a day, how many bales of hay would the farmer have left by the end of December if he starts feeding them this year's hay beginning the first day of September?
    """
    # Calculate the total bales of hay harvested last year
    total_harvest_last_year = 560 * 12

    # Calculate the total bales of hay that can be harvested this year
    total_harvest_this_year = (5 + 7) * 12 * 560 / 5

    # Calculate the total bales of hay available for the horses
    total_hay = total_harvest_last_year + total_harvest_this_year

    # Calculate the total number of bales of hay the horses will consume from September to December
    total_consumed = 9 * 3 * (31 + 30 + 31 + 31)

    # Calculate the total number of bales of hay the farmer will have left by the end of December
    total_left = total_hay - total_consumed

    # Display the total number of bales of hay the farmer will have left
    result = total_left
    return result

print(solution())