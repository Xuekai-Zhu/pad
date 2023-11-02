def solution():
    total_puppies = 8  # John's dog has given birth to 8 puppies
    given_away = total_puppies / 2  # John gives away half of the puppies
    remaining_puppies = total_puppies - given_away  # John keeps the other half of the puppies
    remaining_puppies -= 1  # John keeps one puppy for himself
    
    # Calculate John's profit from selling the remaining puppies
    selling_price = 600  # John sells each puppy for $600
    cost_of_stud = 300  # John pays the owner of the stud $300
    revenue = remaining_puppies * selling_price  # John sells the remaining puppies and earns this much revenue
    profit = revenue - cost_of_stud  # John's profit is the revenue minus the cost of the stud
    
    result = profit
    return result

print(solution())