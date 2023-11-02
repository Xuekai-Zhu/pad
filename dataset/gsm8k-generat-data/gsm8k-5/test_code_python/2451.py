def solution():
    towels_per_wash = 7  # Sanya can wash 7 bath towels in one wash
    wash_time = 1  # One wash takes 1 hour
    available_time = 2  # Sanya has 2 hours a day to wash towels
    total_towels = 98  # Sanya has 98 bath towels in total

    # Calculate the number of washes required
    total_washes = total_towels / towels_per_wash

    # Calculate the number of days required to wash all the towels
    days_required = total_washes * wash_time / available_time
    result = days_required
    return result

print(solution())