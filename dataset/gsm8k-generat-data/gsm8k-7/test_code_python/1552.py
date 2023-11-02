def solution():
    total_people = 180
    # Let's assume x is the number of women working in the company
    # Then, the number of men would be x - 20
    # And the total number of people would be x + x - 20 = 2x - 20

    # Solving for x: 2x - 20 = 180 -> 2x = 200 -> x = 100
    # So, the number of men working in the company would be: 100 - 20 = 80
    num_men = 80
    result = num_men
    return result

print(solution())