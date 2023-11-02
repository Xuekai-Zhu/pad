def solution():
    # Define the original planned production
    planned_production = 200

    # Decrease the production by 50 cars
    decreased_production = planned_production - 50

    # Cut the production by 50% due to pandemic
    final_production = decreased_production * 0.5

    # Calculate the total number of doors produced
    doors_produced = final_production * 5
    result = doors_produced
    return result

print(solution())