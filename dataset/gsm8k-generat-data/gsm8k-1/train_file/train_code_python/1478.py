def solution():
    """Wallace runs a beef jerky company. The company dries the jerky low and slow, so one batch of jerky takes all night to make. Each batch can make 10 bags of jerky. Wallace received a customer order for 60 bags of jerky. If he has 20 bags of jerky already made, how many days will it be before he can fulfill the customer’s order?"""
    batches_needed = (60 - 20) / 10
    days_needed = batches_needed * 1  # assuming one day to make each batch
    result = days_needed
    return result

print(solution())