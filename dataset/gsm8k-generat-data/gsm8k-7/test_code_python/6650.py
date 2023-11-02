def solution():
    starting_inventory = 4500
    monday_sales = 2445
    tuesday_sales = 900
    daily_sales = 50
    supplier_delivery = 650

    # Calculate the total sales for the week from Wednesday to Sunday
    wed_to_sun_sales = 4 * daily_sales

    # Calculate the total sales for the week
    total_sales = monday_sales + tuesday_sales + wed_to_sun_sales

    # Calculate the end inventory after sales
    end_inventory = starting_inventory - total_sales

    # Add the supplier delivery to the end inventory
    end_inventory += supplier_delivery
    result = end_inventory
    return result

print(solution())