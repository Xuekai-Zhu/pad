def solution():
    
    ticket_price = 5
    food_price = 8
    ride_price = 4
    souvenir_price = 15
    food_percentage = 2/3
    ride_percentage = 1/4
    souvenir_percentage = 1/8

    
    total_people = 2520 // ticket_price
    food_people = food_percentage * total_people
    ride_people = ride_percentage * total_people
    souvenir_people = souvenir_percentage * total_people

    
    food_revenue = food_people * food_price
    ride_revenue = ride_people * ride_price
    souvenir_revenue = souvenir_people * souvenir_price

    
    total_revenue = ticket_price * total_people + food_revenue + ride_revenue + souvenir_revenue

    result = total_revenue
    return result

print(solution())