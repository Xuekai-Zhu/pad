def solution():
    """A hay farmer harvested 560 bales of hay from 5 acres of grass per month last year. This year, he planted an additional 7 acres of grass. If the farmer also owns 9 horses and each horse consumes 3 bales of hay a day, how many bales of hay would the farmer have left by the end of December if he starts feeding them this year's hay beginning the first day of September?"""
    # Define the hay yield per acre and the number of acres added
    HAY_YIELD = 560/5
    ACRES_ADDED = 7

    # Calculate the total hay yield for the year
    total_hay_yield = (HAY_YIELD * 12) + (HAY_YIELD * ACRES_ADDED)

    # Calculate the total number of bales of hay needed for the horses
    total_hay_consumption = 9 * 3 * (31+30+31)  

    # Calculate the remaining hay inventory by subtracting the total hay consumption for the horses from the total hay yield
    remaining_hay = total_hay_yield - total_hay_consumption

    # return the result
    result = remaining_hay  
    return result

print(solution())