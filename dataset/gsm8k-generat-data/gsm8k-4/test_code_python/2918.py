def solution():
    """Monica charges $25.00 per person when catering a dinner party. For repeat customers, she offers a 10% discount. Phoebe is a repeat customer who is having a dinner party for 20 guests. How much will Monica make from the party?"""
    # Define the price per person and the number of guests
    price_per_person = 25.00
    num_guests = 20

    # Calculate the total cost before discount
    total_cost = price_per_person * num_guests

    # Apply the discount for repeat customers
    discount = total_cost * 0.1
    total_cost -= discount

    # Calculate the total revenue for Monica
    revenue = total_cost * (1 - 0.3) # 30% deduction for overhead expenses

    result = revenue
    return result

print(solution())