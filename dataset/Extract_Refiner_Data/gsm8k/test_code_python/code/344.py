def solution():
    
    tractors_sold = 10
    tractors_earnings = tractors_sold * 100
    silos_sold = 5
    silos_earnings = silos_sold * 220
    difference = silos_earnings - tractors_earnings
    percent_more = (difference / tractors_sold) * 100
    result = percent_more
    return result

print(solution())