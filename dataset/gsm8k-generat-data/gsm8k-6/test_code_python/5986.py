def solution():
    # Calculate the amount Nancy needs to pay for each semester
    semester_cost = 22000 - 11000 - 3000 - (2*3000) # Tuition cost minus parent contribution, scholarship, and student loan

    # Calculate the amount Nancy needs to earn per hour to pay for tuition
    hourly_rate = semester_cost / 200
    result = hourly_rate
    return result

print(solution())