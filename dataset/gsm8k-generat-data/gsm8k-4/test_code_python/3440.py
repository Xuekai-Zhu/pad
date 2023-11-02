def solution():
    """Mica went to the grocery store and bought 2 kilograms of pasta that costs $1.5; 
    1/4 kilogram of ground beef costs $8 for 1 kilogram; 
    two jars of pasta sauce costs $2 per jar. Mica also wants to buy a $6 Quesadilla for snacks.  
    How much money should she have with her to buy all those?"""
    # Calculate the total cost of the pasta
    pasta_cost = 2 * 1.5

    # Calculate the cost of the ground beef
    beef_cost = 8 * 0.25

    # Calculate the cost of the pasta sauce
    sauce_cost = 2 * 2

    # Calculate the total cost
    total_cost = pasta_cost + beef_cost + sauce_cost + 6

    # return the result
    result = total_cost
    return result

print(solution())