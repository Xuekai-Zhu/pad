def solution():
    # Calculate the original price of pencils before discount
    pencil_price = 20
    num_pencils = 100 / 2
    total_pencil_cost = pencil_price * num_pencils

    # Apply 20% discount on pencils
    discount = 0.2
    discounted_pencil_cost = total_pencil_cost * (1 - discount)

    # Calculate the total cost of all cucumbers
    cucumber_price = 20
    num_cucumbers = 100
    total_cucumber_cost = cucumber_price * num_cucumbers

    # Calculate the total amount spent by Isabela
    total_cost = discounted_pencil_cost + total_cucumber_cost
    result = total_cost
    return result

print(solution())