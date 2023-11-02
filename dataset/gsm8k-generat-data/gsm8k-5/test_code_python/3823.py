def solution():
    days_without_collection = 6  # The garbage truck didn't pass through for 2 weeks or 6 days
    amount_per_collection = 200  # On average, the garbage truck takes 200 kg per collection

    # Calculate the amount of garbage accumulated in the first week
    week_one_amount = amount_per_collection * 3  # The garbage truck collects on Tue, Thu, and Sat
    total_amount_accumulated = week_one_amount

    # Calculate the amount of garbage accumulated in the second week
    week_two_amount = week_one_amount / 2  # People cut their garbage in half
    total_amount_accumulated += week_two_amount

    # Calculate the total amount of garbage accumulated in 2 weeks
    total_amount_accumulated *= days_without_collection
    result = total_amount_accumulated
    return result

print(solution())