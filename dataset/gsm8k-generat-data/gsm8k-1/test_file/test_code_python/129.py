def solution():
    """On Monday, Walt walked 4 miles. Tuesday, he walked 6 times as many miles as he walked on Monday. His total mileage Monday through Wednesday was 41 miles. How many miles did he walk on Wednesday?"""
    monday_miles = 4
    tuesday_miles = 6 * monday_miles
    wednesday_miles = 41 - (monday_miles + tuesday_miles)
    result = wednesday_miles
    return result

print(solution())