def solution():
    """Max is planning a vacation for 8 people. The Airbnb rental costs $3200. They also plan on renting a car that will cost $800. If they plan on splitting the costs equally, how much will each person’s share be?"""
    airbnb_rental_cost = 3200
    car_rental_cost = 800
    total_cost = airbnb_rental_cost + car_rental_cost
    number_of_people = 8
    cost_per_person = total_cost / number_of_people
    result = cost_per_person
    return result

print(solution())