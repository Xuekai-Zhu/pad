def solution():
    """Each member of Greg’s softball team needs to buy one uniform made up of a shirt, a pair of pants, and socks. A shirt costs $7.50, a pair of pants cost $15, and socks cost $4.50 each if each team member buys the uniform items on their own. If they buy the items as a group, they are given a discount. A discounted shirt cost $6.75, a discounted pair of pants cost $13.50, and discounted socks cost $3.75. How much would their team of 12 save with the group discount?"""
    
    # Define the cost of individual items
    shirt_cost = 7.5
    pant_cost = 15
    sock_cost = 4.5

    # Define the cost of discounted items
    discounted_shirt_cost = 6.75
    discounted_pant_cost = 13.5
    discounted_sock_cost = 3.75

    # Define the number of team members
    num_members = 12

    # Calculate the total cost without discount
    total_cost_without_discount = num_members * (shirt_cost + pant_cost + sock_cost)

    # Calculate the total cost with discount
    total_cost_with_discount = num_members * (discounted_shirt_cost + discounted_pant_cost + discounted_sock_cost)

    # Calculate the savings
    savings = total_cost_without_discount - total_cost_with_discount

    # Display the savings
    result = savings
    return result

print(solution())