def solution():
    """At Clark's Food Store, apples cost 40 dollars for a dozen, and pears cost 50 dollars for a dozen. If Hank bought 14 dozen of each kind of fruit, how many dollars did he spend?"""
    # Define the prices of apples and pears per dozen
    apple_price = 40
    pear_price = 50

    # Define the number of dozens of each fruit purchased
    apple_dozen = 14
    pear_dozen = 14

    # Calculate the total cost of the apples and pears
    apple_cost = apple_price * apple_dozen
    pear_cost = pear_price * pear_dozen

    # Calculate the total cost of the purchase
    total_cost = apple_cost + pear_cost

    # return the result
    result = total_cost
    return result

print(solution())