def solution():
    days = 40  # Sharon will be there for 40 days
    pods_per_day = 3  # Sharon drinks 3 pods of coffee every morning
    pods_per_box = 30  # Each box contains 30 pods of coffee
    cost_per_box = 8.00  # Each box of coffee costs $8.00

    # Calculate the total number of pods Sharon will need for the entire vacation
    total_pods = days * pods_per_day

    # Calculate the total number of boxes Sharon will need
    total_boxes = total_pods // pods_per_box  # Use integer division to round down

    # Calculate the total cost of the coffee for the entire vacation
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())