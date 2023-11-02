def solution():
    """Rachel drinks 2 glasses of water on Sunday and 4 glasses of water on Monday. Then she drinks 3 glasses of water every day for the next 4 days. One glass of water is 10 ounces of water. If Rachel wants to drink a total of 220 ounces of water in the week (Sunday to Saturday), how many glasses of water should she drink on Saturday?"""
    sunday = 2
    monday = 4
    tuesday_to_friday = 3 * 4
    total_glasses = sunday + monday + tuesday_to_friday
    total_ounces = total_glasses * 10
    ounces_on_saturday = 220 - total_ounces
    glasses_on_saturday = ounces_on_saturday / 10
    result = glasses_on_saturday
    return result

print(solution())