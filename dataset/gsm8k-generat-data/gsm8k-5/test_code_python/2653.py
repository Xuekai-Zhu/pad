def solution():
    chicken_cost = 16 - (3 * 4) - 1  # Calculate the cost of the chicken by subtracting the cost of beef and oil from the total
    total_cost = chicken_cost + (chicken_cost / 2)  # Calculate the total cost by adding the cost of chicken and dividing it equally among three people
    cost_per_person = total_cost / 3  # Calculate the cost each person should pay
    result = cost_per_person
    return result

print(solution())