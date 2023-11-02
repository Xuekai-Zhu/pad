def solution():
    """James goes out to eat.  He orders a steak and egg meal for $16.  He is with his friend, who orders chicken fried steak for $14.  His friend pays for half the bill and James pays the tip along with his half of the bill. They tip 20%.  How much did James pay?"""
    # Define the cost of each meal
    JAMES_MEAL_COST = 16
    FRIEND_MEAL_COST = 14

    # Calculate the total cost of the meals
    total_cost = JAMES_MEAL_COST + FRIEND_MEAL_COST

    # Calculate the amount James's friend will pay
    friend_payment = total_cost / 2

    # Calculate the cost of the tip
    tip = total_cost * 0.2

    # Calculate the total amount James will pay
    james_payment = friend_payment + tip

    # Display the amount James will pay
    result = james_payment
    return result

print(solution())