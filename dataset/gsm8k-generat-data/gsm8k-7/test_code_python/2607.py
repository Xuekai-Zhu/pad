def solution():
    num_puppies = 8
    puppies_given_away = num_puppies / 2
    remaining_puppies = num_puppies - puppies_given_away - 1  # John keeps one puppy
    price_per_puppy = 600
    stud_owner_fee = 300

    # Calculate the total revenue from selling the remaining puppies
    total_revenue = remaining_puppies * price_per_puppy

    # Calculate the total profit after paying the stud owner fee
    total_profit = total_revenue - stud_owner_fee
    result = total_profit
    return result

print(solution())