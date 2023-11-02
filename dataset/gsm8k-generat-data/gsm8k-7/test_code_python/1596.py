def solution():
    monthly_distance = 400  # kilometers

    # Calculate the total distance Nina would travel in one year
    yearly_distance = (monthly_distance * 10) + (monthly_distance * 20)

    # Calculate the total distance Nina would travel in two years
    total_distance = yearly_distance * 2
    result = total_distance
    return result

print(solution())