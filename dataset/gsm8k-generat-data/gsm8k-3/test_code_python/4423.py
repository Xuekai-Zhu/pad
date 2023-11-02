def solution():
    """Monica and Michelle are combining their money to throw a party. Monica brings $15. Michelle brings $12. The cake costs 15 dollars, and soda is $3 a bottle. Each bottle of soda has 12 servings and they buy as many bottles of soda as they can afford. If there are 8 total guests, how many servings of soda does each get?"""
    # Define the initial amount of money
    monica_money = 15
    michelle_money = 12

    # Define the cost of the cake and the number of guests
    cake_cost = 15
    num_guests = 8

    # Calculate the total amount of money available for soda
    soda_money = monica_money + michelle_money - cake_cost

    # Calculate the maximum number of soda bottles they can buy
    num_soda_bottles = soda_money // 3

    # Calculate the total number of servings of soda
    total_soda_servings = num_soda_bottles * 12

    # Calculate the number of servings of soda each guest gets
    servings_per_guest = total_soda_servings // num_guests

    # Display the number of servings per guest
    result = servings_per_guest
    return result

print(solution())