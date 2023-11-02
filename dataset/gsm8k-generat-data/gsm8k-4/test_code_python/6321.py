def solution():
    """Laura loves to cook. One day she decided to make dinner for her family. She bought the necessary ingredients for this occasion: two salads, 2 kilograms of beef, 1 kilogram of potatoes, and two liters of juice. One salad costs $3, and one kilogram of beef is two times more expensive. One kilogram of potatoes costs one-third of the price of one salad, and one liter of juice is $1.5. How much did Laura need to pay for all the products she bought?"""
    # Define the prices of salads, beef, potatoes, and juice
    salad_price = 3
    beef_price = salad_price * 2
    potato_price = salad_price / 3
    juice_price = 1.5

    # Calculate the total cost of each ingredient
    total_salad_cost = salad_price * 2
    total_beef_cost = beef_price * 2
    total_potato_cost = potato_price * 1
    total_juice_cost = juice_price * 2

    # Calculate the total cost of all ingredients
    total_cost = total_salad_cost + total_beef_cost + total_potato_cost + total_juice_cost

    result = total_cost
    return result

print(solution())