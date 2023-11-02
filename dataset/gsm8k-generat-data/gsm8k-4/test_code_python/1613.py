def solution():
    """ John is a door-to-door salesman. He visits 50 houses a day. 20% of them buy something from them. Of those that buy something half buy a $50 set of knives and the other half buy a $150 set of knives. How much does he sell a week when he works 5 days a week?"""
    # Define the number of houses John visits each week
    weekly_visits = 50 * 5

    # Calculate the number of houses that buy something
    buying_houses = weekly_visits * 0.2

    # Calculate the number of houses that buy the $50 set of knives
    knives50_houses = buying_houses / 2

    # Calculate the number of houses that buy the $150 set of knives
    knives150_houses = buying_houses / 2

    # Calculate the total amount of money John makes from selling the $50 set of knives
    knives50_sales = knives50_houses * 50

    # Calculate the total amount of money John makes from selling the $150 set of knives
    knives150_sales = knives150_houses * 150

    # Calculate the total amount of money John makes in a week
    weekly_sales = knives50_sales + knives150_sales

    result = weekly_sales
    return result

print(solution())