def solution():
    """Laura loves to cook. One day she decided to make dinner for her family. She bought the necessary ingredients for this occasion: two salads, 2 kilograms of beef, 1 kilogram of potatoes, and two liters of juice. One salad costs $3, and one kilogram of beef is two times more expensive. One kilogram of potatoes costs one-third of the price of one salad, and one liter of juice is $1.5. How much did Laura need to pay for all the products she bought?"""
    salad_cost = 3
    beef_cost = salad_cost * 2
    potato_cost = salad_cost / 3
    juice_cost = 1.5
    total_cost = (2 * salad_cost) + (2 * beef_cost) + (1 * potato_cost) + (2 * juice_cost)
    result = total_cost
    return result

print(solution())