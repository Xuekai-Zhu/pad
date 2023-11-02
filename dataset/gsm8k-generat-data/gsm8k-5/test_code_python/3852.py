def solution():
    num_machines = 10  # John has to replace ball bearings for 10 machines
    num_bearings_per_machine = 30  # Each machine takes 30 ball bearings
    regular_price_per_bearing = 1  # Regular price is $1 per bearing
    sale_price_per_bearing = 0.75  # Sale price is $0.75 per bearing
    bulk_discount_percent = 20  # John gets a 20% discount for buying in bulk

    # Calculate the total number of ball bearings needed
    total_bearings_needed = num_machines * num_bearings_per_machine

    # Calculate the total cost with regular price
    regular_price_total = total_bearings_needed * regular_price_per_bearing

    # Calculate the total cost with sale price and bulk discount
    discounted_price_per_bearing = sale_price_per_bearing * (100 - bulk_discount_percent) / 100  # Calculate discounted price per bearing
    discounted_price_total = total_bearings_needed * discounted_price_per_bearing

    # Calculate the amount saved by buying during the sale
    amount_saved = regular_price_total - discounted_price_total
    result = amount_saved
    return result

print(solution())