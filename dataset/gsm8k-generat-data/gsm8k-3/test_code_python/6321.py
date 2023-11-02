def solution():
    """Laura loves to cook. One day she decided to make dinner for her family. She bought the necessary ingredients for this occasion: two salads, 2 kilograms of beef, 1 kilogram of potatoes, and two liters of juice. One salad costs $3, and one kilogram of beef is two times more expensive. One kilogram of potatoes costs one-third of the price of one salad, and one liter of juice is $1.5. How much did Laura need to pay for all the products she bought?"""
    # Define the prices of each ingredient
    SALAD_PRICE = 3
    BEEF_PRICE = SALAD_PRICE * 2
    POTATO_PRICE = SALAD_PRICE/3
    JUICE_PRICE = 1.5

    # Define the amounts of each ingredient purchased
    salad_amount = 2
    beef_amount = 2
    potato_amount = 1
    juice_amount = 2

    # Calculate the total cost of each ingredient
    salad_cost = salad_amount * SALAD_PRICE
    beef_cost = beef_amount * BEEF_PRICE
    potato_cost = potato_amount * POTATO_PRICE
    juice_cost = juice_amount * JUICE_PRICE

    # Calculate the total cost of all ingredients
    total_cost = salad_cost + beef_cost + potato_cost + juice_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())