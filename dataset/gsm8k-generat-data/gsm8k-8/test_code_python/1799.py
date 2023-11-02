def solution():
    # Calculate Guitar Center's total cost
    guitar_center_price = 1000 * (1 - 0.15) + 100

    # Calculate Sweetwater's total cost
    sweetwater_price = 1000 * (1 - 0.1)

    # Calculate the savings from buying from Sweetwater
    savings = guitar_center_price - sweetwater_price
    result = savings
    return result

print(solution())