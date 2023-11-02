def solution():
    """Lyle wants to buy himself and his friends a sandwich and a pack of juice. A sandwich costs $0.30 while a pack of juice costs $0.2. If Lyle has $2.50, how many of his friends can have a sandwich and a pack of juice?"""
    # Define the costs of a sandwich and a pack of juice
    sandwich_cost = 0.3
    juice_cost = 0.2

    # Define the total amount of money Lyle has
    total_money = 2.5

    # Calculate the total cost of one sandwich and one pack of juice
    total_cost = sandwich_cost + juice_cost

    # Calculate the maximum number of friends Lyle can buy for, not including himself
    max_friends = int((total_money - sandwich_cost) / total_cost)

    # Calculate the total number of people, including Lyle, who can have a sandwich and a pack of juice
    total_people = max_friends + 1

    result = total_friends
    return result

print(solution())