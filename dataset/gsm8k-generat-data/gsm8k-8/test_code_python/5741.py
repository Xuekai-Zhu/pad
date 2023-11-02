def solution():
    # Define the costs of the services
    hair_cost = 50
    mani_cost = 30

    # Calculate the tip amounts for each service
    hair_tip = 0.2 * hair_cost
    mani_tip = 0.2 * mani_cost

    # Calculate the total cost of the services with tips included
    total_cost = hair_cost + mani_cost + hair_tip + mani_tip

    result = total_cost
    return result

print(solution())