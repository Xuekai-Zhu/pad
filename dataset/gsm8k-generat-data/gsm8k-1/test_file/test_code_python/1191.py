def solution():
    """Mr. Maxim works at The Best Cookeries Around restaurant. On a particular day, 50 people entered the restaurant in the morning to eat. At around 10:00, 40 more people entered the restaurant and ordered the same amount of food as the first people. After a while, twice the number of people who entered the restaurant at 10:00 came in and ordered lunch. By evening, an additional 3 times as many people as the number that came in first had entered the restaurant. Calculate the total number of people that entered the restaurant on that day."""
    morning_customers = 50
    morning_food = morning_customers
    additional_customers = 40
    additional_food = additional_customers * morning_food
    lunch_customers = 2 * additional_customers
    lunch_food = lunch_customers * morning_food
    evening_customers = 3 * morning_customers
    total_customers = morning_customers + additional_customers + lunch_customers + evening_customers
    result = total_customers
    return result

print(solution())