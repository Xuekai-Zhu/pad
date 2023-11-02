def solution():
    current_price = 4000
    discount = 200

    # Calculate the price of the new camera
    new_price = current_price * 1.3

    # Calculate the total price of the camera and lens, with the discount applied to the lens
    total_price = new_price + (400 - discount)

    result = total_price
    return result

print(solution())