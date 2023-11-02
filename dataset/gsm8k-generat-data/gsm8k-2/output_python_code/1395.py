def solution():
    """Mrs. Lim milks her cows twice a day. Yesterday morning, she got 68 gallons of milk and in the evening, she got 82 gallons. This morning, she got 18 gallons fewer than she had yesterday morning. After selling some gallons of milk in the afternoon, Mrs. Lim has only 24 gallons left. How much was her revenue for the milk if each gallon costs $3.50?"""
    morning1_gallons = 68
    evening_gallons = 82
    morning2_gallons = morning1_gallons - 18
    total_gallons = morning1_gallons + evening_gallons + morning2_gallons - 24
    revenue = total_gallons * 3.5
    result = revenue
    return result

print(solution())