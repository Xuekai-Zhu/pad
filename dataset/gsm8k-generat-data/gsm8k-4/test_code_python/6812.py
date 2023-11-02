def solution():
    """Alice made 52 friendship bracelets over spring break to sell at school. It only cost her $3.00 in materials to make these bracelets. During the break, she gave 8 of her bracelets away. Back at school, she sells all of the remaining bracelets at $0.25 each. How much profit did she make (money earned after paying initial costs) on the sale of her bracelets?"""
    # Define the number of bracelets made, the cost of materials, and the selling price per bracelet
    num_bracelets = 52
    cost_materials = 3.00
    selling_price = 0.25

    # Calculate the number of bracelets given away
    num_given_away = 8

    # Calculate the number of bracelets sold
    num_sold = num_bracelets - num_given_away

    # Calculate the total earnings from selling bracelets
    total_earnings = num_sold * selling_price

    # Calculate the profit by subtracting the cost of materials from the total earnings
    profit = total_earnings - cost_materials

    # return the result
    result = profit
    return result

print(solution())