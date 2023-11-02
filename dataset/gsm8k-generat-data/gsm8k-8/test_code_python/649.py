def solution():
    # Define the number of pencils each student wants
    tolu_pencils = 3
    robert_pencils = 5
    melissa_pencils = 2

    # Calculate the total number of pencils
    total_pencils = tolu_pencils + robert_pencils + melissa_pencils

    # Calculate the total cost of the pencils in cents
    total_cost_cents = total_pencils * 20

    # Convert the total cost to dollars
    total_cost_dollars = total_cost_cents / 100

    result = total_cost_dollars
    return result

print(solution())