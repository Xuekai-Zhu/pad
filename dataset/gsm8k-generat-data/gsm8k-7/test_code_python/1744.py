def solution():
    num_potatoes = 250
    potatoes_per_bundle = 25
    potato_bundle_price = 1.90

    num_carrots = 320
    carrots_per_bundle = 20
    carrot_bundle_price = 2.0

    # Calculate the total number of potato bundles and the total revenue from selling them
    total_potato_bundles = num_potatoes / potatoes_per_bundle
    total_potato_revenue = total_potato_bundles * potato_bundle_price

    # Calculate the total number of carrot bundles and the total revenue from selling them
    total_carrot_bundles = num_carrots / carrots_per_bundle
    total_carrot_revenue = total_carrot_bundles * carrot_bundle_price

    # Calculate the total revenue from selling all harvested crops
    total_revenue = total_potato_revenue + total_carrot_revenue
    result = total_revenue
    return result

print(solution())