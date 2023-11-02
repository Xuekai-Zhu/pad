def solution():
    num_people = 2  # Noah and Ava are both going to the zoo
    ticket_price_per_person = 5  # Tickets cost $5 per person
    bus_fare_per_person = 1.5  # Bus fare costs $1.50 per person one way
    num_round_trips = 2  # They need to take the bus both ways

    # Calculate the total cost of the tickets and bus fare
    total_cost = (num_people * ticket_price_per_person) + (num_people * bus_fare_per_person * num_round_trips)

    # Calculate the amount of money they have left for lunch and snacks
    budget_left = 40 - total_cost
    result = budget_left
    return result

print(solution())