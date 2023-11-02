def solution():
    weekly_charge = 300  # Grace charges 300 dollars per week
    total_to_collect = 1800  # Grace wants to collect 1800 dollars in total
    payment_frequency = 2  # Grace's client pays her every 2 weeks

    # Calculate how many payment cycles Grace needs to complete to collect 1800 dollars
    payment_cycles = total_to_collect / (weekly_charge * payment_frequency)

    # Round up to the nearest whole number of payment cycles
    payment_cycles = math.ceil(payment_cycles)

    # Calculate how many weeks it will take Grace to collect 1800 dollars
    weeks_to_collect = payment_cycles * payment_frequency

    result = weeks_to_collect
    return result

print(solution())