def solution():
    ticket_price = 5  # Price of a single ticket
    food_price = 8  # Price of deep-fried fair food
    ride_price = 4  # Price of a ride
    souvenir_price = 15  # Price of a souvenir

    # Proportions of ticket-buyers who purchase each item
    food_proportion = 2 / 3
    ride_proportion = 1 / 4
    souvenir_proportion = 1 / 8

    total_income = 2520  # Total income from ticket sales

    # Solve for the number of tickets sold
    total_tickets = total_income / ticket_price

    # Calculate the income from food, rides, and souvenirs
    food_income = total_tickets * food_proportion * food_price
    ride_income = total_tickets * ride_proportion * ride_price
    souvenir_income = total_tickets * souvenir_proportion * souvenir_price

    # Calculate the total income
    total_income += food_income + ride_income + souvenir_income
    result = total_income
    return result

print(solution())