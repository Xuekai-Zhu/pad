def solution():
    """John's dog has a litter of 8 puppies. He gives away half of them. He keeps one of the remaining puppies. He then takes the remaining puppies and sells them each for $600. He had to give the owner of the stud $300. How much money does he profit?"""
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