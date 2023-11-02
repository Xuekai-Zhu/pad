def solution():
    """Krista started raising chickens. She has 10 hens who lay eggs. She sells the eggs for $3 a dozen. In four weeks, she sold $120 worth of eggs. If she sold all the eggs her hens laid, how many eggs does each hen lay a week?"""
    num_hens = 10
    selling_price = 3  # Price per dozen
    total_sales = 120
    num_weeks = 4
    num_eggs_per_week = (total_sales / selling_price) / num_weeks / num_hens
    result = num_eggs_per_week
    return result

print(solution())