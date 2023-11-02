def solution():
    """James goes out to eat. He orders a steak and egg meal for $16. He is with his friend, who orders chicken fried steak for $14. His friend pays for half the bill and James pays the tip along with his half of the bill. They tip 20%. How much did James pay?"""
    # Define the cost of James' meal and his friend's meal
    james_meal = 16
    friend_meal = 14

    # Calculate the total cost of the meal
    total_cost = james_meal + friend_meal

    # Calculate James' half of the total cost
    james_half = total_cost / 2

    # Calculate the tip amount
    tip_amount = james_half * 0.2

    # Calculate James' final amount to pay
    james_final = james_half + tip_amount

    result = james_final
    return result

print(solution())