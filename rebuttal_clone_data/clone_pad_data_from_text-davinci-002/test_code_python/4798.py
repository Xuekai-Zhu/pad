def solution():
     milk_collected = 30000
     milk_pumped = 2880
     milk_added = 1500
     milk_left = milk_collected + milk_added - milk_pumped
     result = milk_left
     return result

print(solution())