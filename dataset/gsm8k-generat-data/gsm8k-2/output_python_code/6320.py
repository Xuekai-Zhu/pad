def solution():
    """Laura loves to cook. One day she decided to make dinner for her family. She bought the necessary ingredients for this occasion: two salads, 2 kilograms of beef, 1 kilogram of potatoes, and two liters of juice.
    One salad costs $3, and one kilogram of beef is two times more expensive.
    One kilogram of potatoes costs one-third of the price of one salad, and one liter of juice is $1.5.
    How much did Laura need to pay for all the products she bought?"""
    salad_price = 3
    beef_price = 2 * salad_price
    potato_price = salad_price / 3
    juice_price = 1.5
    total_price = (2 * salad_price) + (2 * beef_price) + (1 * potato_price) + (2 * juice_price)
    result = total_price
    return result

print(solution())