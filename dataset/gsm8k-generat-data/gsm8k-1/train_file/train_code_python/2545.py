def solution():
    """Jack makes his own cold brew coffee. He makes it in batches of 1.5 gallons. He drinks 96 ounces of coffee every 2 days. It takes 20 hours to make coffee. How long does he spend making coffee over 24 days?"""
    batch_size_gallons = 1.5
    batch_size_ounces = batch_size_gallons * 128
    coffee_consumed_2_days = 96
    days_24 = 24
    batches_per_day = 24 / 2
    total_batches = batches_per_day * days_24
    total_coffee = total_batches * batch_size_ounces
    coffee_making_time = 20
    time_spent_making_coffee = coffee_making_time * total_batches
    result = time_spent_making_coffee
    
    return result

print(solution())