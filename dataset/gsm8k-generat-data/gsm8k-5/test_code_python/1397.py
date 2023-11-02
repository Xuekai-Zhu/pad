def solution():
    # Calculate the total volume of soup
    milk = 2  # Marly adds 2 quarts of milk
    vegetables = 1  # Marly starts with 1 quart of pureed vegetables
    stock = 3 * vegetables  # Marly adds 3 times as much chicken stock as vegetables
    total_volume = milk + vegetables + stock

    # Calculate the number of bags needed to hold the soup
    bag_size = 3  # Marly wants to use bags that can hold 3 quarts each
    bags_needed = total_volume / bag_size
    result = bags_needed
    return result

print(solution())