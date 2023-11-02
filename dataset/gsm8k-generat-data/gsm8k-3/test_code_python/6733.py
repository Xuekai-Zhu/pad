def solution():
    """Tommy has a flag that is 5 feet wide and 4 feet tall. He wants to paint it with a new design. He knows from experience that he needs to paint both sides. Paint costs $2 a quart and a quart is good for 4 square feet. How much does he spend on paint?"""
    # Define the dimensions of the flag
    width = 5
    height = 4

    # Calculate the total area of the flag (both sides)
    total_area = 2 * width * height

    # Calculate the total amount of paint needed in quarts
    paint_needed = total_area / 4

    # Calculate the total cost of the paint
    paint_cost = paint_needed * 2

    # Display the total cost of the paint
    result = paint_cost
    return result

print(solution())