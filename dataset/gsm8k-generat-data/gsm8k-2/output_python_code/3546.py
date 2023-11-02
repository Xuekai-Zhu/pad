def solution():
    """
    James gets a fleet of gas transportation vans. He gets 6 vans. 2 of them are 8000 gallons. 1 of them is 30% less than that.
    The remaining trucks are 50% larger than the 2 trucks. How many gallons can he transport?
    """
    van_1 = 8000
    van_2 = 8000
    van_3 = van_1 * 0.7
    total_van_1_2 = van_1 + van_2
    total_remaining_vans = 3 * 1.5 * total_van_1_2
    total_gallons = total_van_1_2 + van_3 + total_remaining_vans
    result = total_gallons
    return result

print(solution())