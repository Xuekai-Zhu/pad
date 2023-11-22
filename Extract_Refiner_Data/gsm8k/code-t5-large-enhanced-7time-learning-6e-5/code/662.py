def solution():
    
    # Define the amount of money Aurelia has
    arelia_money = 120

    # Calculate the amount of money Kassidy has
    kassidy_money = arelia_money * 0.75

    # Calculate the amount of money Rayna has
    rayna_money = kassidy_money + 60

    # Calculate the total amount of money they have together
    total_money = arelia_money + kassidy_money + rayna_money

    # Calculate the amount of money each person would have if they added together their money
    each_person_money = total_money / 2

    # Display the amount of money each person would have if they share equally
    result = each_person_money
    return result

print(solution())