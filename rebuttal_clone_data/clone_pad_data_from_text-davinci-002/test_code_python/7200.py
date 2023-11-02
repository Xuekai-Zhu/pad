def solution():
     owen_start = 21
     johanna_start = owen_start - 5
     owen_end = owen_start * 2
     johanna_end = johanna_start / 2
     owen_gain = owen_end - owen_start
     johanna_loss = johanna_start - johanna_end
     owen_final = owen_end + johanna_loss
     result = owen_final
     return result

print(solution())