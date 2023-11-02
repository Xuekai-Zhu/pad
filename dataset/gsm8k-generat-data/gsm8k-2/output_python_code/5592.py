def solution():
    """A father is building a playset for his son and needs to purchase lumber, nails, and fabric. When he started planning the project, the necessary lumber cost $450, the nails cost $30, and the fabric cost $80. However, recent economic inflation has caused the price of lumber to increase by 20%, the price of nails to increase by 10%, and the price of fabric to increase by 5%. In dollars, how much more money will it cost to complete the project now (after inflation) than it would have when the father began planning?"""
    initial_lumber_cost = 450
    initial_nails_cost = 30
    initial_fabric_cost = 80
    lumber_inflation = 0.2
    nails_inflation = 0.1
    fabric_inflation = 0.05
    inflated_lumber_cost = initial_lumber_cost * (1 + lumber_inflation)
    inflated_nails_cost = initial_nails_cost * (1 + nails_inflation)
    inflated_fabric_cost = initial_fabric_cost * (1 + fabric_inflation)
    total_initial_cost = initial_lumber_cost + initial_nails_cost + initial_fabric_cost
    total_inflated_cost = inflated_lumber_cost + inflated_nails_cost + inflated_fabric_cost
    difference = total_inflated_cost - total_initial_cost
    result = difference
    return result

print(solution())