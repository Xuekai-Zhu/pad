def solution():
    pasta_amount = 2 # in kg
    pasta_price = 1.5 # per kg

    beef_amount = 1/4 # in kg
    beef_price = 8 # per kg

    sauce_amount = 2 # in jars
    sauce_price = 2 # per jar

    quesadilla_price = 6

    # Calculate the total cost of pasta
    pasta_cost = pasta_amount * pasta_price

    # Calculate the total cost of ground beef
    beef_cost = beef_amount * beef_price

    # Calculate the total cost of pasta sauce
    sauce_cost = sauce_amount * sauce_price

    # Calculate the total cost of all items
    total_cost = pasta_cost + beef_cost + sauce_cost + quesadilla_price
    result = total_cost
    return result

print(solution())