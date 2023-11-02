def solution():
    doris_spent = 6  # Doris spent $6
    martha_spent = doris_spent / 2  # Martha spent half as much as Doris
    remaining_money = 15  # There were $15 left in the cookie jar
    total_money = remaining_money + doris_spent + martha_spent  # Total money in the cookie jar

    # Calculate the initial amount of money in the cookie jar
    initial_money = total_money - doris_spent - martha_spent
    result = initial_money
    return result

print(solution())