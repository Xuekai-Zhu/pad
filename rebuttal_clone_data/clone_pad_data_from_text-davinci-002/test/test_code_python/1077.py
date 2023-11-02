def solution():
 
    copper_pipe = 40
    num_tightening_bolts = copper_pipe / 5
    num_washers_per_bolt = 2
    total_num_washers = num_tightening_bolts * num_washers_per_bolt
    washers_in_bag = 20
    washers_left_in_bag = washers_in_bag - total_num_washers
 
    result = washers_left_in_bag
 
    return result

print(solution())