def solution():
    """Jack makes his own cold brew coffee. He makes it in batches of 1.5 gallons. He drinks 96 ounces of coffee every 2 days. It takes 20 hours to make coffee. How long does he spend making coffee over 24 days?"""
    batch_size = 1.5 * 128  # Convert gallons to ounces
    consumption_rate = 96 / 2  # Ounces per day
    time_to_make_one_batch = 20  # Hours
    days_to_make_one_batch = time_to_make_one_batch / 24  # Convert hours to days

    batches_in_24_days = 24 // days_to_make_one_batch

    ounces_in_24_days = consumption_rate * 12  # 24 days = 12 two-day periods
    total_batches_needed = ounces_in_24_days / batch_size
    total_batches_made = min(total_batches_needed, batches_in_24_days)

    time_spent_making_coffee = total_batches_made * time_to_make_one_batch

    result = time_spent_making_coffee
    return result

print(solution())