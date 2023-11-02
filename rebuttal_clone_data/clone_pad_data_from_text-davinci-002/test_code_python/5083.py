def solution():
    
     initial_price = 15
     final_price = 65
     bid_increment = 5
     number_of_bids = (final_price - initial_price) / bid_increment
     number_of_bids_per_person = number_of_bids / 2
     result = number_of_bids_per_person
     return result

print(solution())