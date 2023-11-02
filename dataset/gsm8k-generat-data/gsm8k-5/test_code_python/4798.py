def solution():
    initial_milk = 30000  # Initial milk collected by the workers, in gallons
    pumped_out = 2880 * 4  # Milk pumped out, in gallons
    milk_added = 1500 * 7  # Milk added after pumping, in gallons

    # Calculate the total milk left in the storage tank
    total_milk = initial_milk - pumped_out + milk_added
    result = total_milk
    return result

print(solution())