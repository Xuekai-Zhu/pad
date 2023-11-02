def solution():
    """Julia just adopted a puppy for $20.00 from the local pet shelter.  Before she brings the puppy home, she needs to buy a bag of dog food for $20.00, 2 bags of treats for $2.50 a bag, an assortment box of toys for $15.00, a crate and a bed for $20.00 each, and the collar/leash combo for $15.00.  The store offered Julia a 20% new-customer discount.  How much will Julia spend on the new puppy?"""
    # Define the costs of each item
    PUPPY_PRICE = 20
    DOG_FOOD_PRICE = 20
    TREATS_PRICE = 2.5
    TOY_PRICE = 15
    CRATE_PRICE = 20
    BED_PRICE = 20
    COLLAR_LEASH_PRICE = 15

    # Calculate the total cost of all items without the discount
    total_cost_without_discount = PUPPY_PRICE + DOG_FOOD_PRICE + (2 * TREATS_PRICE) + TOY_PRICE + (2 * CRATE_PRICE) + COLLAR_LEASH_PRICE + BED_PRICE

    # Calculate the 20% discount
    discount = total_cost_without_discount * 0.2

    # Calculate the total cost after the discount
    total_cost_with_discount = total_cost_without_discount - discount

    # Return the total cost after the discount
    return total_cost_with_discount

print(solution())