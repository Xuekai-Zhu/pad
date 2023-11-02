def solution():
    """The Martin family goes to the mall to get ice cream. A kiddie scoop is $3. A regular scoop is $4. A double scoop is $6. Mr. and Mrs. Martin each get the regular scoop. Their two children each get the kiddie scoop. Their three teenage children each get double scoops. How much money does Mrs. Martin pay the cashier?"""
    # Define the prices of each ice cream scoop
    KIDDIE_PRICE = 3
    REGULAR_PRICE = 4
    DOUBLE_PRICE = 6

    # Calculate the total cost for each family member
    mr_martin_cost = REGULAR_PRICE
    mrs_martin_cost = REGULAR_PRICE
    child_cost = KIDDIE_PRICE * 2
    teen_cost = DOUBLE_PRICE * 3

    # Calculate the total cost for the entire family
    total_cost = mr_martin_cost + mrs_martin_cost + child_cost + teen_cost

    # return the result
    result = total_cost
    return result

print(solution())