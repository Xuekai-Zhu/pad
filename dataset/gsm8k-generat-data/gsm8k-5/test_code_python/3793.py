def solution():
    rental_cost = 3200  # Airbnb rental costs $3200
    car_rental_cost = 800  # The car rental costs $800
    total_cost = rental_cost + car_rental_cost  # Calculate the total cost
    num_people = 8  # There are 8 people splitting the cost

    # Divide the total cost by the number of people to calculate each person's share
    share_per_person = total_cost / num_people
    result = share_per_person
    return result

print(solution())