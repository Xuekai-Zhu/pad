def solution():
    # Calculate the number of cars produced after the first cut
    cars_produced = 200 - 50  # 50 cars production decreased
    # Calculate the number of cars produced after the pandemic cut
    cars_produced *= 0.5  # production decreased by 50%
    # Calculate the total number of doors produced
    total_doors_produced = cars_produced * 5  # each car has 5 doors
    result = total_doors_produced
    return result

print(solution())