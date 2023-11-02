def solution():
    """Alice made 52 friendship bracelets over spring break to sell at school.  It only cost her $3.00 in materials to make these bracelets.  During the break, she gave 8 of her bracelets away.  Back at school, she sells all of the remaining bracelets at $0.25 each.  How much profit did she make (money earned after paying initial costs) on the sale of her bracelets?"""
    # Define the number of bracelets made and the cost of materials
    num_bracelets = 52
    material_cost = 3.0

    # Calculate the number of bracelets given away
    given_bracelets = 8

    # Calculate the number of bracelets sold
    sold_bracelets = num_bracelets - given_bracelets

    # Calculate the total revenue from the sale of the bracelets
    revenue = sold_bracelets * 0.25

    # Calculate the profit from the sale of the bracelets
    profit = revenue - material_cost

    # Display the profit
    result = profit
    return result

print(solution())