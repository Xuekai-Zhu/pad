def solution():
    # Define the products of General Motors and movie theaters
    gm_products = ["automobiles", "automobile parts", "financial services"]
    movie_theater_products = ["movie tickets", "snacks", "beverages"]
    # Check if any of General Motors products are sold at movie theaters
    for product in gm_products:
        if product in movie_theater_products:
            result = "yes"
            break
    else:
        result = "no"
    return result

print(solution())