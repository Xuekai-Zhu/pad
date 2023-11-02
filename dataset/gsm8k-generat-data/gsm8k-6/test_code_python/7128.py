def solution():
    # Calculate the cost of primer and paint for 5 rooms
    gallons_of_primer = 5  # each room requires a gallon of primer
    gallons_of_paint = 5  # each room requires a gallon of paint
    cost_of_primer = 0.8 * 30 * gallons_of_primer  # 20% discount on primer
    cost_of_paint = 25 * gallons_of_paint
    total_cost = cost_of_primer + cost_of_paint
    result = total_cost
    return result

print(solution())