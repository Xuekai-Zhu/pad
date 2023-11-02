def solution():
    delta_flight = 850
    united_flight = 1100
    delta_discount = 20
    united_discount = 30
    delta_saving = delta_flight * (delta_discount / 100)
    united_saving = united_flight * (united_discount / 100)
    total_saving = delta_saving + united_saving
    result = total_saving
    return result

print(solution())