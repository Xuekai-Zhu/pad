def solution():
    """Sarah, Mary, and Tuan decided to go to the restaurant for a meal. They decided to split the cost of the meal evenly. If the total price of the meal comes to $67 and they have a coupon for $4, how much does each person need to contribute to the bill?"""
    # Define the cost of the meal and the value of the coupon
    meal_cost = 67
    coupon_value = 4

    # Calculate the total cost after the coupon is applied
    total_cost = meal_cost - coupon_value

    # Determine the number of people splitting the bill
    num_people = 3

    # Calculate the amount each person needs to contribute
    per_person_cost = total_cost / num_people

    # Display the amount each person needs to contribute
    result = per_person_cost
    return result

print(solution())