def solution():
    bikes_sold = 8
    bike_painting_pay = 5
    bike_selling_pay = 8 + bike_painting_pay
    total_pay = bikes_sold * bike_selling_pay
    result = total_pay
    return result

print(solution())