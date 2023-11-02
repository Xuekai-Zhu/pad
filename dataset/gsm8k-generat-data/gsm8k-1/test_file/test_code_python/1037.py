def solution():
    """Molly is catering a birthday party for her sister and invited 16 people. 10 people want the chicken salad which is $6.50 per person and 6 people want the pasta salad at $6 per person. What is the total amount Molly will pay for the catering?"""
    num_chicken_salad = 10
    price_chicken_salad = 6.5
    num_pasta_salad = 6
    price_pasta_salad = 6
    total_guests = num_chicken_salad + num_pasta_salad
    total_cost = (num_chicken_salad * price_chicken_salad) + (num_pasta_salad * price_pasta_salad)
    result = total_cost
    return result

print(solution())