def solution():
     red_roses = 12
     pink_roses = 18
     yellow_roses = 20
     orange_roses = 8
     
     total_roses = red_roses + pink_roses + yellow_roses + orange_roses
     
     percent_red = 50
     percent_pink = 50
     percent_yellow = 25
     percent_orange = 25
     
     num_red = total_roses * (percent_red/100)
     num_pink = total_roses * (percent_pink/100)
     num_yellow = total_roses * (percent_yellow/100)
     num_orange = total_roses * (percent_orange/100)
     total_picked = num_red + num_pink + num_yellow + num_orange
     
     result = total_picked
     return result

print(solution())