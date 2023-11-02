def solution():
    # Define the initial amount of money Christian and Sue have
    christian_money = 5
    sue_money = 7

    # Calculate the amount of money Christian and Sue made from their jobs
    christian_job_money = 4 * 5
    sue_job_money = 6 * 2

    # Calculate the total amount of money Christian and Sue have
    total_money = christian_money + sue_money + christian_job_money + sue_job_money

    # Calculate the difference between the total money and the cost of the perfume
    difference = 50 - total_money
    
    result = difference
    return result

print(solution())