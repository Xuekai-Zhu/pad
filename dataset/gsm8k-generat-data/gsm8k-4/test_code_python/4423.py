def solution():
    """Monica and Michelle are combining their money to throw a party. Monica brings $15. Michelle brings $12. The cake costs 15 dollars, and soda is $3 a bottle. Each bottle of soda has 12 servings and they buy as many bottles of soda as they can afford. If there are 8 total guests, how many servings of soda does each get?"""
    # Define the initial amount of money Monica and Michelle have
    monica_money = 15
    michelle_money = 12

    # Define the cost of the cake
    cake_cost = 15

    # Define the cost of one bottle of soda and the number of servings in each bottle
    soda_cost = 3
    soda_servings = 12

    # Calculate the total amount of money available for soda after buying the cake
    total_money = monica_money + michelle_money - cake_cost

    # Calculate the maximum number of soda bottles they can afford
    max_soda_bottles = int(total_money / soda_cost)

    # Calculate the total number of soda servings
    total_soda_servings = max_soda_bottles * soda_servings

    # Calculate the number of servings each guest gets
    servings_per_guest = total_soda_servings / 8

    # return the result
    result = servings_per_guest
    return result

print(solution())