def solution():
    # Define initial vegetable intake per day
    asparagus_intake = 0.25
    broccoli_intake = 0.25

    # Double vegetable intake after 2 weeks
    asparagus_intake *= 2
    broccoli_intake *= 2

    # Calculate total vegetable intake per week after adding kale
    total_veggies = (asparagus_intake + broccoli_intake) * 7 + 3

    result = total_veggies
    return result

print(solution())