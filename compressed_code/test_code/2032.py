def solution():
    
    initial_puppies = 8
    given_away_puppies = initial_puppies // 2
    remaining_puppies = initial_puppies - given_away_puppies
    kept_puppy = 1
    puppies_sold = remaining_puppies - kept_puppy
    puppy_price = 600
    stud_fee = 300
    total_profit = (puppies_sold * puppy_price) - stud_fee
    result = total_profit
    return result

print(solution())