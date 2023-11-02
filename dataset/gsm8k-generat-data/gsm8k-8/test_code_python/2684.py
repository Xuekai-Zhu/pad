def solution():
    # Define variables
    ticket_price = 5
    food_price = 8
    ride_price = 4
    souvenir_price = 15
    food_fraction = 2/3
    ride_fraction = 1/4
    souvenir_fraction = 1/8
    total_income = 2520

    # Calculate the number of people who bought tickets (and hence the total number of people)
    total_people = total_income / ticket_price

    # Calculate the number of people who bought food, rode a ride, or bought a souvenir
    food_people = food_fraction * total_people
    ride_people = ride_fraction * total_people
    souvenir_people = souvenir_fraction * total_people

    # Calculate the total income from food, rides, and souvenirs
    food_income = food_people * food_price
    ride_income = ride_people * ride_price
    souvenir_income = souvenir_people * souvenir_price

    # Calculate the total income from all sources
    total_income = total_income + food_income + ride_income + souvenir_income
    result = total_income
    return result

print(solution())