def solution():
    """Julia just adopted a puppy for $20.00 from the local pet shelter. Before she brings the puppy home, she needs to buy a bag of dog food for $20.00, 2 bags of treats for $2.50 a bag, an assortment box of toys for $15.00, a crate and a bed for $20.00 each, and the collar/leash combo for $15.00. The store offered Julia a 20% new-customer discount. How much will Julia spend on the new puppy?"""
    puppy_cost = 20
    dog_food_cost = 20
    treat_cost = 2.5 * 2
    toy_cost = 15
    crate_cost = 20
    bed_cost = 20
    collar_leash_cost = 15
    total_cost = puppy_cost + dog_food_cost + treat_cost + toy_cost + crate_cost + bed_cost + collar_leash_cost
    discount = total_cost * 0.2
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())