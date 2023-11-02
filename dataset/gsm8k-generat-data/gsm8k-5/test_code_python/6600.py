def solution():
    shepherd_pie_slices = 4  # Each Shepherd's pie is cut into 4 pieces
    chicken_pie_slices = 5  # Each Chicken pot pie is cut into 5 pieces
    shepherd_pie_orders = 52  # 52 customers ordered slices of shepherd's pie
    chicken_pie_orders = 80  # 80 customers ordered slices of chicken pot pie

    # Calculate the total number of Shepherd's pies sold
    total_shepherd_pies = shepherd_pie_orders / shepherd_pie_slices

    # Calculate the total number of Chicken pot pies sold
    total_chicken_pies = chicken_pie_orders / chicken_pie_slices

    # Calculate the total number of pies sold
    total_pies = total_shepherd_pies + total_chicken_pies
    result = total_pies
    return result

print(solution())