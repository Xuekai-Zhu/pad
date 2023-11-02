def solution():
    """A farmer harvested 250 potatoes. He bundled them in twenty-five's and sold each bundle for $1.90. He also harvested 320 carrots and bundled them in twenty's and sold each bundle for $2. If the farmer sold all his harvested crops, how much did he get in all?"""
    # Define the number of potatoes per bundle and the price per bundle
    POTATOES_PER_BUNDLE = 25
    POTATO_PRICE_PER_BUNDLE = 1.9

    # Calculate the number of potato bundles and the total cost
    potato_bundles = 250 // POTATOES_PER_BUNDLE
    potato_cost = potato_bundles * POTATO_PRICE_PER_BUNDLE

    # Define the number of carrots per bundle and the price per bundle
    CARROTS_PER_BUNDLE = 20
    CARROT_PRICE_PER_BUNDLE = 2

    # Calculate the number of carrot bundles and the total cost
    carrot_bundles = 320 // CARROTS_PER_BUNDLE
    carrot_cost = carrot_bundles * CARROT_PRICE_PER_BUNDLE

    # Calculate the total earnings
    total_earnings = potato_cost + carrot_cost

    # Display the total earnings
    result = total_earnings
    return result

print(solution())