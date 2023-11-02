def solution():
    num_pumpkins = 83
    carving_price = 3
    total_carving_sales = 96

    # Calculate the total revenue from selling pumpkins for carving
    total_carving_revenue = num_pumpkins * carving_price

    # Calculate the number of pumpkins remaining after carving sales
    remaining_pumpkins = num_pumpkins - (total_carving_sales / carving_price)

    # Calculate the number of cans of pie filling that can be made from the remaining pumpkins
    cans_of_pie_filling = remaining_pumpkins // 3
    result = cans_of_pie_filling
    return result

print(solution())