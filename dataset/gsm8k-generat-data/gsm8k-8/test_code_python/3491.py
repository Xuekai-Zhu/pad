def solution():
    # Calculate the number of guests who like weak coffee and strong coffee
    num_weak_coffee = 12 / 2
    num_strong_coffee = 12 / 2

    # Calculate the total amount of coffee needed for the weak coffee
    weak_coffee_amount = num_weak_coffee * 1

    # Calculate the total amount of coffee needed for the strong coffee
    strong_coffee_amount = num_strong_coffee * 2

    # Calculate the total amount of coffee needed
    total_coffee_amount = weak_coffee_amount + strong_coffee_amount
    result = total_coffee_amount
    return result

print(solution())