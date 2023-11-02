def solution():
    """A math teacher had $100 to buy three different types of calculators. A basic calculator costs $8. A scientific calculator costs twice the price as the basic while a graphing calculator costs thrice the price as the scientific. How much change did she receive after buying those three different types of calculators?"""
    # Define the prices of the calculators
    BASIC_PRICE = 8
    SCIENTIFIC_PRICE = BASIC_PRICE * 2
    GRAPHING_PRICE = SCIENTIFIC_PRICE * 3

    # Define the amount of money the teacher has to spend
    total_money = 100

    # Calculate the maximum number of basic calculators the teacher can buy
    max_basic = total_money // BASIC_PRICE

    # Calculate the maximum number of scientific calculators the teacher can buy
    max_scientific = total_money // SCIENTIFIC_PRICE

    # Calculate the maximum number of graphing calculators the teacher can buy
    max_graphing = total_money // GRAPHING_PRICE

    # Calculate the total cost of the calculators
    total_cost = max_basic * BASIC_PRICE + max_scientific * SCIENTIFIC_PRICE + max_graphing * GRAPHING_PRICE

    # Calculate the change the teacher will receive
    change = total_money - total_cost

    # Display the change
    result = change
    return result

print(solution())