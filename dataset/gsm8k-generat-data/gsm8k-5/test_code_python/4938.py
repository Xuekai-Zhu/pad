def solution():
    total_cartons = 400  # Kayden's business processed 400 cartons of milk
    cartons_per_customer = total_cartons / 4  # The cartons were divided equally among four customers
    damaged_cartons = 60  # Each customer returned 60 cartons damaged

    # Calculate the total number of cartons accepted by the customers (before damages)
    total_accepted_cartons = cartons_per_customer * 4

    # Subtract the number of damaged cartons from the total accepted cartons
    net_accepted_cartons = total_accepted_cartons - (damaged_cartons * 4)
    result = net_accepted_cartons
    return result

print(solution())