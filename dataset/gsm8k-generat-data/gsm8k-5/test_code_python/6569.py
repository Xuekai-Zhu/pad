def solution():
    price_per_person = 147  # The original price is $147 per person
    discount = 14  # Each of them gets a discount of $14
    num_people = 2  # There are two people, Ali and Leila

    # Calculate the total cost after the discount
    total_cost = (price_per_person - discount) * num_people

    result = total_cost
    return result

print(solution())