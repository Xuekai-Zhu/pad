def solution():
    # Calculate the subtotal (total before tax)
    subtotal = 80 + 10

    # Calculate the tax
    tax = subtotal * 0.1

    # Calculate the total bill (including tax)
    total = subtotal + tax

    # Calculate the gratuity charge (assuming 20% tip)
    gratuity = total * 0.2

    result = gratuity
    return result

print(solution())