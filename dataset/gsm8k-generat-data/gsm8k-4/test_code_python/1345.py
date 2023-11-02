def solution():
    """Mimi has decided to start going to the gym again. Over the weekend, she spent $8,000 on athletic sneakers and clothes. She spent thrice as much on Nike sneakers as she did on Adidas. What she spent on Adidas was 1/5 the cost of Skechers. If Mimi's Adidas sneakers purchase was $600, what amount did she spend on clothes?"""
    # Define the cost of Adidas sneakers
    adidas_cost = 600

    # Calculate the cost of Skechers sneakers
    skechers_cost = 5 * adidas_cost

    # Calculate the cost of Nike sneakers
    nike_cost = 3 * adidas_cost

    # Calculate the total cost of sneakers
    total_sneakers_cost = adidas_cost + skechers_cost + nike_cost

    # Calculate the cost of clothes
    clothes_cost = 8000 - total_sneakers_cost

    # return the result
    result = clothes_cost
    return result

print(solution())