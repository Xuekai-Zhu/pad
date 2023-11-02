def solution():
    """Heisenberg owns a pharmacy. He earned a total of $80 from 100 mg amoxicillin and $60 from 500 mg amoxicillin every week. If each capsule of 100 mg amoxicillin costs $5 and each capsule of 500 mg amoxicillin costs $2, how many capsules of amoxicillin does he sell every 2 weeks?"""
    # Define the price and earnings of 100 mg and 500 mg amoxicillin
    price_100mg = 5
    price_500mg = 2
    earnings_100mg_per_week = 80
    earnings_500mg_per_week = 60

    # Calculate the number of capsules sold every week
    capsules_100mg_per_week = earnings_100mg_per_week / price_100mg
    capsules_500mg_per_week = earnings_500mg_per_week / price_500mg

    # Calculate the total number of capsules sold every 2 weeks
    total_capsules = (capsules_100mg_per_week + capsules_500mg_per_week) * 2

    result = total_capsules
    return result

print(solution())