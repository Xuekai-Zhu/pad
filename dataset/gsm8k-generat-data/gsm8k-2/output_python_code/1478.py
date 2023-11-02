def solution():
    """Wallace runs a beef jerky company. The company dries the jerky low and slow, so one batch of jerky takes all night to make. Each batch can make 10 bags of jerky. Wallace received a customer order for 60 bags of jerky. If he has 20 bags of jerky already made, how many days will it be before he can fulfill the customer’s order?"""
    total_jerky_needed = 60
    jerky_already_made = 20
    jerky_per_batch = 10
    batches_needed = (total_jerky_needed - jerky_already_made) / jerky_per_batch
    days_needed = int(batches_needed + 0.9)  # round up to nearest day
    result = days_needed
    return result

print(solution())