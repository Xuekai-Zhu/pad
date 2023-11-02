def solution():
    # Calculate the total revenue from selling necklaces
    necklaces_sold = 5
    price_per_necklace = 25
    total_necklace_revenue = necklaces_sold * price_per_necklace

    # Calculate the total revenue from selling bracelets
    bracelets_sold = 10
    price_per_bracelet = 15
    total_bracelet_revenue = bracelets_sold * price_per_bracelet

    # Calculate the total revenue from selling earrings
    earrings_sold = 20
    price_per_earring = 10
    total_earring_revenue = earrings_sold * price_per_earring

    # Calculate the revenue from the two jewelry ensembles
    jewelry_ensembles_sold = 2
    price_per_ensemble = 45
    total_ensemble_revenue = jewelry_ensembles_sold * price_per_ensemble

    # Calculate the total revenue over the weekend
    total_revenue = (
        total_necklace_revenue
        + total_bracelet_revenue
        + total_earring_revenue
        + total_ensemble_revenue
    )
    result = total_revenue
    return result

print(solution())