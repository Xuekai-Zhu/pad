def solution():
    """A state fair charges $5 for a ticket. Two-thirds of the people who buy a ticket will buy deep-fried fair food for $8,
    one quarter will go on a ride for $4, and one eighth will spend $15 on a souvenir. The fair made $2520 from tickets.
    How many dollars did they make in all?"""
    ticket_price = 5
    food_price = 8
    ride_price = 4
    souvenir_price = 15
    food_percentage = 2/3
    ride_percentage = 1/4
    souvenir_percentage = 1/8

    # calculating the number of people who bought each item
    total_people = 2520 // ticket_price
    food_people = food_percentage * total_people
    ride_people = ride_percentage * total_people
    souvenir_people = souvenir_percentage * total_people

    # calculating the total revenue from each item
    food_revenue = food_people * food_price
    ride_revenue = ride_people * ride_price
    souvenir_revenue = souvenir_people * souvenir_price

    # calculating the total revenue
    total_revenue = ticket_price * total_people + food_revenue + ride_revenue + souvenir_revenue

    result = total_revenue
    return result

print(solution())