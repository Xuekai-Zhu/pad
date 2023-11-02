def solution():
    """Julia just adopted a puppy for $20.00 from the local pet shelter. Before she brings the puppy home, she needs to buy a bag of dog food for $20.00, 2 bags of treats for $2.50 a bag, an assortment box of toys for $15.00, a crate and a bed for $20.00 each, and the collar/leash combo for $15.00. The store offered Julia a 20% new-customer discount. How much will Julia spend on the new puppy?"""
    adopted_puppy_cost = 20
    dog_food_cost = 20
    treats_cost = 2.5 * 2
    toys_cost = 15
    crate_cost = 20
    bed_cost = 20
    collar_leash_cost = 15
    total_cost = adopted_puppy_cost + dog_food_cost + treats_cost + toys_cost + crate_cost + bed_cost + collar_leash_cost
    discount = total_cost * 0.2
    total_cost = total_cost - discount
    result = total_cost
    return result

print(solution())