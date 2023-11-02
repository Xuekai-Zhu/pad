def solution():
    netflix_cost = 10  # Tim gets Netflix for $10 a month
    hulu_disney_cost = 10  # Tim gets Hulu and Disney Plus normally cost $10 a month each
    discount = 0.2  # Tim saves 20% for bundling
    cable_package = 60  # Tim cancelling his $60 cable package

    # Calculate the total cost of getting Netflix and disney Plus for a month
    total_cost = netflix_cost + (hulu_disney_cost * discount)

    # Calculate the amount Tim saves by cancelling his $60 cable package
    savings = total_cost * 0.2
    result = savings
    return result

print(solution())