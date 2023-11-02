def solution():
    # Define the amount of money Rene received
    rene_money = 300

    # Calculate how much Maria gave to Isha
    isha_money = 1/3 * (3 * rene_money)
    
    # Calculate how much Florence received
    florence_money = 1/2 * isha_money

    # Calculate the total amount of money Maria gave to her friends
    total_money = isha_money + florence_money + rene_money
    result = total_money
    return result

print(solution())