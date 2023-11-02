def solution():
    pencil_price = 0.20  # Price of one pencil

    # Number of pencils each student wants
    tolu_pencils = 3
    robert_pencils = 5
    melissa_pencils = 2

    # Total number of pencils
    total_pencils = tolu_pencils + robert_pencils + melissa_pencils

    # Total cost of pencils
    total_cost = total_pencils * pencil_price

    result = total_cost
    return result

print(solution())