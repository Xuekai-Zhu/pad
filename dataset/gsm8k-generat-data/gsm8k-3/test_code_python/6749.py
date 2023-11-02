def solution():
    """James buys twice as many toy soldiers as toy cars. He buys 20 toy cars. How many total toys does he buy?"""
    # Define the number of toy cars purchased
    car_count = 20

    # Calculate the number of toy soldiers purchased (twice as many as toy cars)
    soldier_count = car_count * 2

    # Calculate the total number of toys purchased
    total_toys = car_count + soldier_count

    # Display the total number of toys purchased
    result = total_toys
    return result

print(solution())