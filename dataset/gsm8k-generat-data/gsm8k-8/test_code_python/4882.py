def solution():
    # Calculate the number of shoppers who prefer to use the express lane
    express_shoppers = 0.625 * 480

    # Calculate the number of shoppers who pay at the check-out lane
    checkout_shoppers = 480 - express_shoppers
    result = checkout_shoppers
    return result

print(solution())