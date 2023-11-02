def solution():
    """A father is building a playset for his son and needs to purchase lumber, nails, and fabric. When he started planning the project, the necessary lumber cost $450, the nails cost $30, and the fabric cost $80. However, recent economic inflation has caused the price of lumber to increase by 20%, the price of nails to increase by 10%, and the price of fabric to increase by 5%. In dollars, how much more money will it cost to complete the project now (after inflation) than it would have when the father began planning?"""
    # Define the original prices and the inflation rates
    lumber_original = 450
    nails_original = 30
    fabric_original = 80
    lumber_inflation = 0.2
    nails_inflation = 0.1
    fabric_inflation = 0.05

    # Calculate the new prices after inflation
    lumber_new = lumber_original * (1 + lumber_inflation)
    nails_new = nails_original * (1 + nails_inflation)
    fabric_new = fabric_original * (1 + fabric_inflation)

    # Calculate the total difference in cost
    cost_difference = (lumber_new + nails_new + fabric_new) - (lumber_original + nails_original + fabric_original)

    result = cost_difference
    return result

print(solution())