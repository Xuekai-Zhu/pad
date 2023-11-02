def solution():
    """James started a food fight in his school's cafeteria, and the school administration is making him work off the cost of all the food he wasted at minimum wage ($8). James has to pay for 20 wasted pounds of meat at $5/pound, 15 wasted pounds of fruits and vegetables at $4/pound, 60 wasted pounds of bread products at $1.50/pound, and 10 hours of time-and-a-half pay for the janitorial staff, who normally make $10/hour. How many hours will James have to work to pay for everything?"""
    # Define the cost of each type of wasted food per pound
    MEAT_PRICE = 5
    FRUIT_VEGGIE_PRICE = 4
    BREAD_PRICE = 1.5

    # Define the number of pounds of each type of wasted food
    meat_pounds = 20
    fruit_veggie_pounds = 15
    bread_pounds = 60

    # Calculate the cost of the wasted meat
    meat_cost = meat_pounds * MEAT_PRICE

    # Calculate the cost of the wasted fruits and vegetables
    fruit_veggie_cost = fruit_veggie_pounds * FRUIT_VEGGIE_PRICE

    # Calculate the cost of the wasted bread products
    bread_cost = bread_pounds * BREAD_PRICE

    # Calculate the cost of the janitorial staff's time
    janitorial_pay = 10 * 1.5 * 10  # 10 hours at time-and-a-half pay of $15/hour

    # Calculate the total cost of everything
    total_cost = meat_cost + fruit_veggie_cost + bread_cost + janitorial_pay

    # Calculate the number of hours James will have to work to pay for everything
    hours_worked = total_cost / 8  # minimum wage is $8/hour

    # Display the number of hours James will have to work
    result = hours_worked
    return result

print(solution())