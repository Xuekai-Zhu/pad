def solution():
    adoption_fee = 20.0
    dog_food_cost = 20.0
    num_treat_bags = 2
    treat_bag_cost = 2.5
    toy_box_cost = 15.0
    num_crates = 1
    crate_cost = 20.0
    num_beds = 1
    bed_cost = 20.0
    collar_leash_cost = 15.0
    new_customer_discount = 0.2  # 20% discount

    # Calculate the total cost of all items without the adoption fee
    total_cost = dog_food_cost + (num_treat_bags * treat_bag_cost) + toy_box_cost + (num_crates * crate_cost) \
                 + (num_beds * bed_cost) + collar_leash_cost

    # Apply the new-customer discount
    total_cost = total_cost * (1 - new_customer_discount)

    # Add the adoption fee to the total cost
    total_cost += adoption_fee
    result = total_cost
    return result

print(solution())