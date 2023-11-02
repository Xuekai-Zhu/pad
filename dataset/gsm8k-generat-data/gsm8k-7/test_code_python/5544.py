def solution():
    total_potatoes = 6500
    damaged_potatoes = 150
    good_potatoes = total_potatoes - damaged_potatoes
    bag_weight = 50
    bag_price = 72
    
    # Calculate the total number of bags of potatoes
    total_bags = good_potatoes // bag_weight
    
    # Calculate the total amount of money made from selling the potatoes
    total_sale_amount = total_bags * bag_price
    result = total_sale_amount
    return result

print(solution())