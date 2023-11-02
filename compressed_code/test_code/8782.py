def solution():
    
    airbnb_rental_cost = 3200
    car_rental_cost = 800
    total_cost = airbnb_rental_cost + car_rental_cost
    number_of_people = 8
    cost_per_person = total_cost / number_of_people
    result = cost_per_person
    return result

print(solution())