def solution():
    # Define the balloon bag options and their corresponding prices and quantities
    balloon_bags = {'small': {'price': 4, 'quantity': 50},
                    'medium': {'price': 6, 'quantity': 75},
                    'extra_large': {'price': 12, 'quantity': 200}}

    # Initialize variables for maximum number of balloons and total cost
    max_balloons = 0
    total_cost = 0

    # Loop through all possible combinations of bag sizes and quantities to find the maximum number of balloons within budget
    for s in range(0, 9):
        for m in range(0, 5):
            for xl in range(0, 3):
                if s * balloon_bags['small']['price'] + m * balloon_bags['medium']['price'] + xl * balloon_bags['extra_large']['price'] <= 24:
                    num_balloons = s * balloon_bags['small']['quantity'] + m * balloon_bags['medium']['quantity'] + xl * balloon_bags['extra_large']['quantity']
                    if num_balloons > max_balloons:
                        max_balloons = num_balloons

    result = max_balloons
    return result

print(solution())