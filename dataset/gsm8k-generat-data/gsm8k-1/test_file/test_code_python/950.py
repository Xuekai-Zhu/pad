def solution():
    """Jonathan has 2/3 as many measuring spoons as measuring cups. If he has two dozen cups and gifts Pedro 6 measuring spoons for his birthday, calculate the total number of utensils Jonathan has remaining."""
    measuring_cups = 2*12
    measuring_spoons = (2/3) * measuring_cups
    measuring_spoons_gifted = 6
    total_utensils = measuring_cups + measuring_spoons - measuring_spoons_gifted
    result = total_utensils
    return result

print(solution())