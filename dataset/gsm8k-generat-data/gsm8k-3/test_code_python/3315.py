def solution():
    """A factory manufactures cars with 5 doors. The factory was planning to produce 200 cars but due to metal shortages, they decreased the production by 50 cars. Due to a pandemic, they also had to cut production by another 50%. How many doors will the factory produce?"""
    # Define the number of doors per car
    DOORS_PER_CAR = 5

    # Define the initial planned production and the production losses
    initial_production = 200
    metal_shortage_loss = 50
    pandemic_loss_percentage = 0.5

    # Calculate the actual production after losses
    actual_production = (initial_production - metal_shortage_loss) * (1 - pandemic_loss_percentage)

    # Calculate the total number of doors produced
    total_doors = actual_production * DOORS_PER_CAR

    # Display the total number of doors produced
    result = total_doors
    return result

print(solution())