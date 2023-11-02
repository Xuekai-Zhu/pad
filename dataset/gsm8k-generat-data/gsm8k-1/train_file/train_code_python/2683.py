def solution():
    """A state fair charges $5 for a ticket. Two-thirds of the people who buy a ticket will buy deep-fried fair food for $8, one quarter will go on a ride for $4, and one eighth will spend $15 on a souvenir. The fair made $2520 from tickets. How many dollars did they make in all?"""
    ticket_price = 5
    food_price = 8
    ride_price = 4
    souvenir_price = 15
    food_percent = 2 / 3
    ride_percent = 1 / 4
    souvenir_percent = 1 / 8
    total_tickets_sold = 2520 / ticket_price
    total_spent_on_food = total_tickets_sold * food_percent * food_price
    total_spent_on_rides = total_tickets_sold * ride_percent * ride_price
    total_spent_on_souvenirs = total_tickets_sold * souvenir_percent * souvenir_price
    total_money_made = (total_tickets_sold * ticket_price) + total_spent_on_food + total_spent_on_rides + total_spent_on_souvenirs
    result = total_money_made
    return result

print(solution())