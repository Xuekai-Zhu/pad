def solution():
    """James started a food fight in his school's cafeteria, and the school administration is making him work off the cost of all the food he wasted at minimum wage ($8). James has to pay for 20 wasted pounds of meat at $5/pound, 15 wasted pounds of fruits and vegetables at $4/pound, 60 wasted pounds of bread products at $1.50/pound, and 10 hours of time-and-a-half pay for the janitorial staff, who normally make $10/hour. How many hours will James have to work to pay for everything?"""
    meat_cost = 20 * 5
    fruits_veggies_cost = 15 * 4
    bread_cost = 60 * 1.5
    total_food_cost = meat_cost + fruits_veggies_cost + bread_cost
    
    janitor_pay = 10 * 1.5 * 10
    
    total_cost = total_food_cost + janitor_pay
    
    hours_worked = total_cost / 8
    
    result = hours_worked
    return result

print(solution())