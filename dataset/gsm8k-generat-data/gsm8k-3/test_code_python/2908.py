def solution():
    """Andrew holds a bake sale to fundraise for charity. The bake sale earns a total of $400. Andrew keeps $100 to cover the cost of ingredients. He donates half of the remaining total to the local homeless shelter, and the other half to the local food bank. Andrew also decides to donate $10 from his own piggy bank to the local homeless shelter. How much money in total does Andrew donate to the homeless shelter?"""
    # Define the total earnings and the cost of ingredients
    total_earnings = 400
    ingredient_cost = 100

    # Calculate the total amount left after the cost of ingredients is deducted
    remainder = total_earnings - ingredient_cost

    # Calculate the amount donated to the homeless shelter, including Andrew's personal donation
    shelter_donation = (remainder / 2) + 10

    # Display the total amount donated to the homeless shelter
    result = shelter_donation
    return result

print(solution())