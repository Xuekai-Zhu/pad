def solution():
    """Stormi is saving up to buy a bicycle. She washes 3 cars for $10 each. She mows 2 lawns for $13 each. If the bicycle she wants costs $80, how much more money does Stormi need to make to afford the bicycle?"""
    # Define the amount of money Stormi makes from washing cars and mowing lawns
    car_money = 3 * 10
    lawn_money = 2 * 13

    # Calculate the total amount of money she has saved up
    total_money = car_money + lawn_money

    # Calculate the amount of money she still needs to save up
    remaining_money = 80 - total_money

    # Display the remaining amount of money she needs to make
    result = remaining_money
    return result

print(solution())