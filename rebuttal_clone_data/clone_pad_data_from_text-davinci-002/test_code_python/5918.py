def solution():
     minutes_pulling_chain = 15
     minutes_not_pulling_chain = 10
     ascent_rate = 50
     descent_rate = 10
     total_ascent = minutes_pulling_chain * ascent_rate
     total_descent = minutes_not_pulling_chain * descent_rate
     result = total_ascent - total_descent
     return result

print(solution())