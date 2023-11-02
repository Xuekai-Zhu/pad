def solution():
    # Calculate the total number of house guests
    total_guests = 12*2  # 12 guests who like weak coffee and 12 guests who like strong coffee

    # Calculate the number of tablespoons of coffee needed for weak coffee
    weak_coffee = 12*1  # 1 tablespoon of coffee per cup for weak coffee

    # Calculate the number of tablespoons of coffee needed for strong coffee
    strong_coffee = 12*2  # double the amount for strong coffee

    # Calculate the total number of tablespoons of coffee needed
    total_coffee = weak_coffee + strong_coffee

    result = total_coffee
    return result

print(solution())