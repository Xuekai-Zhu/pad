def solution():
    """A state fair charges $5 for a ticket. Two-thirds of the people who buy a ticket will buy deep-fried fair food for $8, one quarter will go on a ride for $4, and one eighth will spend $15 on a souvenir. The fair made $2520 from tickets. How many dollars did they make in all?"""
    # Define the prices of fair food, rides, and souvenirs
    FOOD_PRICE = 8
    RIDE_PRICE = 4
    SOUVENIR_PRICE = 15

    # Define the proportions of people who buy fair food, go on a ride, and buy a souvenir
    FOOD_PROPORTION = 2/3
    RIDE_PROPORTION = 1/4
    SOUVENIR_PROPORTION = 1/8

    # Calculate the revenue from ticket sales
    ticket_revenue = 2520

    # Calculate the total number of people who bought tickets
    total_people = ticket_revenue / 5

    # Calculate the number of people who bought fair food
    food_people = total_people * FOOD_PROPORTION

    # Calculate the number of people who went on a ride
    ride_people = total_people * RIDE_PROPORTION

    # Calculate the number of people who bought a souvenir
    souvenir_people = total_people * SOUVENIR_PROPORTION

    # Calculate the total revenue from fair food
    food_revenue = food_people * FOOD_PRICE

    # Calculate the total revenue from rides
    ride_revenue = ride_people * RIDE_PRICE

    # Calculate the total revenue from souvenirs
    souvenir_revenue = souvenir_people * SOUVENIR_PRICE

    # Calculate the total revenue
    total_revenue = ticket_revenue + food_revenue + ride_revenue + souvenir_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())