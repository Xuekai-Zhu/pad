def solution():
    # Calculate the total number of cars sold per month by all sales professionals
    cars_per_month = 10 * 10  # each salesperson sells 10 cars per month

    # Calculate the total number of months it will take to sell all cars
    total_months = 500 / cars_per_month

    # Round up to the nearest integer
    total_months = int(total_months + 0.5)

    result = total_months
    return result

print(solution())