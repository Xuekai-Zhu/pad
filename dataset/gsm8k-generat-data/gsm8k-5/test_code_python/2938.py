def solution():
    annual_salary = 150000  # Mike's annual salary is $150,000
    saving_percentage = 0.1  # Mike saves 10% of his salary
    down_payment_percentage = 0.2  # Mike needs to save a down payment of 20% of the house cost
    house_cost = 450000  # The cost of the house Mike wants to buy is $450,000

    # Calculate the amount of money Mike saves per year
    savings_per_year = annual_salary * saving_percentage

    # Calculate the amount of money Mike needs to save for the down payment
    down_payment = house_cost * down_payment_percentage

    # Calculate the number of years it will take for Mike to save for the down payment
    years_to_save = down_payment / savings_per_year
    result = years_to_save
    return result

print(solution())