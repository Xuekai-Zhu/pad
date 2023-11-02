def solution():
    pineapple_cost = 6  # Cost of pineapple juice per glass
    mango_cost = 5  # Cost of mango juice per glass
    total_spent = 94  # Total amount spent by the group
    pineapple_spent = 54  # Amount spent on pineapple juice

    # Calculate the number of glasses of pineapple juice ordered
    pineapple_glasses = pineapple_spent / pineapple_cost

    # Calculate the number of glasses of mango juice ordered
    mango_glasses = (total_spent - pineapple_spent) / mango_cost

    # Calculate the total number of people in the group
    total_people = pineapple_glasses + mango_glasses

    result = total_people
    return result

print(solution())