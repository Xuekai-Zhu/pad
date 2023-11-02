def solution():
    # Define total cost of the car and amount already saved
    total_cost = 14600
    saved = 14500

    # Define the number of trips Alex will make and the fee per trip
    num_trips = 40
    trip_fee = 1.5

    # Calculate the total amount earned from trip fees
    total_trip_fee = num_trips * trip_fee

    # Calculate the total amount earned from the 5% commission on groceries
    total_grocery_cost = (total_cost - saved - total_trip_fee) / 0.05

    result = total_grocery_cost
    return result

print(solution())