def solution():
    """Jenny's property tax rate is 2%. Her house is currently worth $400,000. The city is about to build a new high-speed rail project nearby, which will increase her house's value by 25%. Jenny can only afford to spend $15,000/year on property tax. How many dollars worth of improvements can she make to her house before her property tax bill gets too high?"""
    # Define the initial house value and the property tax rate
    house_value = 400000
    tax_rate = 0.02

    # Calculate the new house value after the high-speed rail project
    new_value = house_value * 1.25

    # Initialize the maximum affordable improvement amount
    improvement_amount = 0

    # Calculate the maximum affordable improvement amount by comparing property tax costs
    while house_value + improvement_amount <= new_value:
        # Calculate the new property tax cost
        new_tax_cost = (house_value + improvement_amount) * tax_rate

        # Add the improvement amount to the total
        improvement_amount += 1000

        # Break the loop if the new tax cost exceeds the affordable limit
        if new_tax_cost > 15000:
            improvement_amount -= 1000
            break

    # Display the maximum affordable improvement amount
    result = improvement_amount
    return result

print(solution())