def solution():
    # Calculate the original cost of the pencils before discount
    pencil_cost = 20
    total_pencil_cost = pencil_cost * 2
    # Calculate the discounted cost of the pencils
    discounted_pencil_cost = total_pencil_cost * 0.8

    # Calculate the total cost of cucumbers
    cucumber_cost = 20
    total_cucumber_cost = cucumber_cost * 100

    # Calculate the total amount spent on items
    total_spent = discounted_pencil_cost + total_cucumber_cost
    result = total_spent
    return result

print(solution())