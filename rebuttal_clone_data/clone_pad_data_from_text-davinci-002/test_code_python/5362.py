def solution():
     euston = 130
     norfolk = euston - 20
     norwich = norfolk + 100
     flying_scotsman = norwich + 20
     total_carriages = euston + norfolk + norwich + flying_scotsman
     result = total_carriages
     return result

print(solution())