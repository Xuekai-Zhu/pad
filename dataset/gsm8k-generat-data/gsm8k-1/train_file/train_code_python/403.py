def solution():
    """A hay farmer harvested 560 bales of hay from 5 acres of grass per month last year. This year, he planted an additional 7 acres of grass. If the farmer also owns 9 horses and each horse consumes 3 bales of hay a day, how many bales of hay would the farmer have left by the end of December if he starts feeding them this year's hay beginning the first day of September?"""
    previous_harvest = 560
    previous_acres = 5
    additional_acres = 7
    total_acres = previous_acres + additional_acres
    current_harvest = (total_acres / previous_acres) * previous_harvest
    hay_needed_per_day = 9 * 3
    hay_needed_from_sept_to_dec = hay_needed_per_day * 30 * 4
    hay_needed_total = hay_needed_from_sept_to_dec + 560 # Including leftover hay from last year
    hay_leftover = current_harvest - hay_needed_total
    result = hay_leftover
    return result

print(solution())