def solution():
    # Calculate the total number of potato bundles
    potato_bundles = 250 / 25

    # Calculate the total revenue from potato sales
    potato_revenue = potato_bundles * 1.9

    # Calculate the total number of carrot bundles
    carrot_bundles = 320 / 20

    # Calculate the total revenue from carrot sales
    carrot_revenue = carrot_bundles * 2

    # Calculate the total revenue from all crop sales
    total_revenue = potato_revenue + carrot_revenue
    result = total_revenue
    return result

print(solution())