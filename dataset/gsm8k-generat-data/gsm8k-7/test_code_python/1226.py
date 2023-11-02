def solution():
    necklace_price = 25
    num_necklaces = 5

    bracelet_price = 15
    num_bracelets = 10

    earrings_price = 10
    num_earrings = 20

    jewelry_ensemble_price = 45
    num_jewelry_ensemble = 2

    # Calculate the total revenue from necklaces sold
    total_necklace_revenue = necklace_price * num_necklaces

    # Calculate the total revenue from bracelets sold
    total_bracelet_revenue = bracelet_price * num_bracelets

    # Calculate the total revenue from earrings sold
    total_earrings_revenue = earrings_price * num_earrings

    # Calculate the total revenue from jewelry ensembles sold
    total_ensemble_revenue = jewelry_ensemble_price * num_jewelry_ensemble

    # Calculate the total revenue from all sales
    total_revenue = total_necklace_revenue + total_bracelet_revenue + total_earrings_revenue + total_ensemble_revenue
    result = total_revenue
    return result

print(solution())