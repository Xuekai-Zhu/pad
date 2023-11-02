def solution():
    initial_milk = 30000
    pumping_rate = 2880
    pumping_time = 4
    adding_rate = 1500
    adding_time = 7

    # Calculate the total amount of milk pumped out of the storage tank
    pumped_milk = pumping_rate * pumping_time

    # Calculate the total amount of milk added to the storage tank
    added_milk = adding_rate * adding_time

    # Calculate the remaining milk in the storage tank
    remaining_milk = initial_milk - pumped_milk + added_milk
    result = remaining_milk
    return result

print(solution())