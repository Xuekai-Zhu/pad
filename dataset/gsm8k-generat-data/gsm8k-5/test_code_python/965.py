def solution():
    total_cost = 67  # The total cost of the meal is $67
    discount = 4  # They have a $4 coupon
    actual_cost = total_cost - discount  # The actual cost after the discount is applied
    num_of_people = 3  # There are 3 people splitting the cost equally

    # Calculate the amount each person needs to contribute
    per_person_cost = actual_cost / num_of_people
    result = per_person_cost
    return result

print(solution())