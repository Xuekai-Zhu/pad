def solution():
    # Calculate the amount spent on mango juice
    mango_amount = 94 - 54  # total amount spent - amount spent on pineapple juice
    mango_price = 5  # price of mango juice
    mango_count = mango_amount / mango_price  # number of glasses of mango juice bought

    # Calculate the number of glasses of pineapple juice bought
    pineapple_price = 6  # price of pineapple juice
    pineapple_count = 54 / pineapple_price  # number of glasses of pineapple juice bought

    # Calculate the total number of people in the group
    total_people = mango_count + pineapple_count
    result = total_people
    return result

print(solution())