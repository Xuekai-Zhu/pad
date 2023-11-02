def solution():
    # Define the costs of each type of scoop
    kiddie_cost = 3
    regular_cost = 4
    double_cost = 6

    # Calculate the total cost for each family member
    mr_martin_cost = regular_cost
    mrs_martin_cost = regular_cost
    child1_cost = kiddie_cost
    child2_cost = kiddie_cost
    teen1_cost = double_cost
    teen2_cost = double_cost
    teen3_cost = double_cost

    # Calculate the total cost for the whole family
    total_cost = mr_martin_cost + mrs_martin_cost + child1_cost + child2_cost + teen1_cost + teen2_cost + teen3_cost

    # Return the amount Mrs. Martin pays
    result = mrs_martin_cost
    return result

print(solution())