def solution():
    actor_cost = 1200  # The cost of hiring actors is $1200
    num_people = 50  # There are 50 people for whom food needs to be provided
    food_cost = num_people * 3  # The cost of providing food is $3 per person
    equipment_rental = 2 * (actor_cost + food_cost)  # Equipment rental costs twice as much as actors and food combined
    total_cost = actor_cost + food_cost + equipment_rental  # The total cost of making the movie
    revenue = 10000  # They sold the movie for $10000
    profit = revenue - total_cost  # The profit they made from selling the movie

    result = profit
    return result

print(solution())