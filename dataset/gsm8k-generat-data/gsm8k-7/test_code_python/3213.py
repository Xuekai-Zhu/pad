def solution():
    slices_per_pumpkin_pie = 8
    slices_per_custard_pie = 6
    price_per_pumpkin_pie_slice = 5
    price_per_custard_pie_slice = 6
    num_pumpkin_pies = 4
    num_custard_pies = 5

    # Calculate the total number of pumpkin pie slices sold
    total_pumpkin_slices_sold = num_pumpkin_pies * slices_per_pumpkin_pie

    # Calculate the total number of custard pie slices sold
    total_custard_slices_sold = num_custard_pies * slices_per_custard_pie

    # Calculate the total revenue from pumpkin pie sales
    revenue_from_pumpkin_pies = total_pumpkin_slices_sold * price_per_pumpkin_pie_slice

    # Calculate the total revenue from custard pie sales
    revenue_from_custard_pies = total_custard_slices_sold * price_per_custard_pie_slice

    # Calculate the total revenue from all pie sales
    total_revenue = revenue_from_pumpkin_pies + revenue_from_custard_pies
    result = total_revenue
    return result

print(solution())