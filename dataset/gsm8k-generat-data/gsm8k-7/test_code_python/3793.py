def solution():
    num_people = 8
    airbnb_cost = 3200
    car_rental_cost = 800

    # Calculate the total cost of the vacation
    total_cost = airbnb_cost + car_rental_cost

    # Calculate each person's share of the total cost
    share_per_person = total_cost / num_people
    result = share_per_person
    return result

print(solution())