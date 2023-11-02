def solution():
    starting_gallons = 10
    gas_used_to_store = 6
    gas_used_to_doctor = 2
    total_gallons_used = gas_used_to_store + gas_used_to_doctor

    max_gallons = 12
    gallons_needed = max_gallons - (starting_gallons - total_gallons_used)
    result = gallons_needed
    return result

print(solution())