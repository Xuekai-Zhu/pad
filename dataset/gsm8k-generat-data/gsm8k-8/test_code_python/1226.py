def solution():
    # Calculate the total sales from each type of jewelry
    necklace_sales = 5 * 25
    bracelet_sales = 10 * 15
    earring_sales = 20 * 10

    # Calculate the sales from the complete jewelry ensembles
    ensemble_sales = 2 * 45

    # Calculate the total sales for the weekend
    total_sales = necklace_sales + bracelet_sales + earring_sales + ensemble_sales
    result = total_sales
    return result

print(solution())