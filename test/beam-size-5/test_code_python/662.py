def solution():
    
    # Define the amount of money Aurelia has
    aurelia_money = 120

    # Calculate the amount of money Kassidy has
    kassidy_money = aurelia_money * 3/4

    # Calculate the amount of money Rayna has
    rayna_money = kassidy_money + 60

    # Calculate the total amount of money they have
    total_money = aurelia_money + kassidy_money + rayna_money

    # Calculate how much each person would have if they share equally
    each_money = total_money / 2

    # Display how much each person would have
    result = each_money
    return result

print(solution())