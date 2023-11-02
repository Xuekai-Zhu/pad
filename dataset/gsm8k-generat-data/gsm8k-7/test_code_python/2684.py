def solution():
    ticket_price = 5
    food_price = 8
    ride_price = 4
    souvenir_price = 15
    total_ticket_sales = 2520
    
    # Calculate the number of people who bought tickets
    num_tickets = total_ticket_sales / ticket_price
    
    # Calculate the number of people who bought deep-fried fair food
    num_food = (2 / 3) * num_tickets
    
    # Calculate the number of people who went on a ride
    num_rides = (1 / 4) * num_tickets
    
    # Calculate the number of people who bought a souvenir
    num_souvenirs = (1 / 8) * num_tickets
    
    # Calculate the total revenue from food sales
    food_sales = num_food * food_price
    
    # Calculate the total revenue from ride sales
    ride_sales = num_rides * ride_price
    
    # Calculate the total revenue from souvenir sales
    souvenir_sales = num_souvenirs * souvenir_price
    
    # Calculate the total revenue from all sales
    total_sales = total_ticket_sales + food_sales + ride_sales + souvenir_sales
    result = total_sales
    return result

print(solution())