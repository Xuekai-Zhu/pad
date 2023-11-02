def solution():
    """A father is building a playset for his son and needs to purchase lumber, nails, and fabric.  When he started planning the project, the necessary lumber cost $450, the nails cost $30, and the fabric cost $80.  However, recent economic inflation has caused the price of lumber to increase by 20%, the price of nails to increase by 10%, and the price of fabric to increase by 5%.  In dollars, how much more money will it cost to complete the project now (after inflation) than it would have when the father began planning?"""
    # Define the original costs
    original_lumber_cost = 450
    original_nails_cost = 30
    original_fabric_cost = 80

    # Calculate the new costs with inflation
    new_lumber_cost = original_lumber_cost * 1.2
    new_nails_cost = original_nails_cost * 1.1
    new_fabric_cost = original_fabric_cost * 1.05

    # Calculate the difference between the new and original costs
    cost_difference = (new_lumber_cost + new_nails_cost + new_fabric_cost) - \
                      (original_lumber_cost + original_nails_cost + original_fabric_cost)

    # Display the cost difference
    result = cost_difference
    return result

print(solution())