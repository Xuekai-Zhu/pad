def solution(): 
     new_frame_price = 60 * 1.2
     smaller_frame_price = new_frame_price * 0.75
     money_remaining = 60 - smaller_frame_price
     result = money_remaining
     return result

print(solution())