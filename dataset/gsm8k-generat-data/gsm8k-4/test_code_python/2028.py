def solution():
    """Eliza buys 200 ornamental rings to sell in their local shop, twice the number of the remaining stock. After selling 3/4 of the total stock, her mother buys 300 more ornamental rings, and after three days, sells 150. What's the total number of ornamental rings remaining in the store?"""
    # Define the initial number of rings
    initial_stock = None

    # Calculate the number of rings Eliza buys
    eliza_buys = 200

    # Calculate the number of rings before Eliza's purchase
    rings_before_eliza = eliza_buys * 0.5

    # Calculate the total number of rings
    total_rings = initial_stock + rings_before_eliza + eliza_buys

    # Calculate the number of rings sold by Eliza
    eliza_sales = total_rings * 0.75

    # Calculate the number of rings after Eliza's sales
    rings_after_eliza = total_rings - eliza_sales

    # Calculate the number of rings after Eliza's mother's purchase
    rings_after_mother = rings_after_eliza + 300

    # Calculate the number of rings after mother's sales
    rings_after_sales = rings_after_mother - 150

    # Return the remaining number of rings
    result = rings_after_sales
    return result

print(solution())