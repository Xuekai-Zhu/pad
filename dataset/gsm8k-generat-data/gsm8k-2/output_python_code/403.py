def solution():
    """A hay farmer harvested 560 bales of hay from 5 acres of grass per month last year. This year, he planted an additional 7 acres of grass. If the farmer also owns 9 horses and each horse consumes 3 bales of hay a day, how many bales of hay would the farmer have left by the end of December if he starts feeding them this year's hay beginning the first day of September?"""
    hay_per_acre = 560 / 5
    total_hay_yield = hay_per_acre * 12 + (hay_per_acre + 7) * 4
    total_hay_needed = 9 * 3 * (30*4 + 31*3 + 30*3)
    hay_left = total_hay_yield - total_hay_needed
    result = hay_left
    return result

print(solution())