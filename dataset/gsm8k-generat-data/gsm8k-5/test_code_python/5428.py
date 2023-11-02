def solution():
    # Andy walks 50 meters to school and then back, so he walks 100 meters to school and back
    distance_to_school = 50
    distance_to_market = 140 - 100  # Andy walks a total of 140 meters, so he walks 40 meters to the market
    distance_between_house_and_market = distance_to_market - distance_to_school
    result = distance_between_house_and_market
    return result

print(solution())