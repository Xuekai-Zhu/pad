def solution():
    mango_price = 5
    pineapple_price = 6
    total_spent = 94
    pineapple_spent = 54

    # Calculate the total spent on mango juice
    mango_spent = total_spent - pineapple_spent

    # Calculate the number of glasses of mango juice
    num_mango_glasses = mango_spent / mango_price

    # Calculate the number of glasses of pineapple juice
    num_pineapple_glasses = pineapple_spent / pineapple_price

    # Calculate the total number of people in the group
    total_people = num_mango_glasses + num_pineapple_glasses
    result = total_people
    return result

print(solution())