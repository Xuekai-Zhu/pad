def solution():
     onion_time = 20
     garlic_pepper_time = onion_time / 4
     kneading_time = 30
     resting_time = kneading_time * 2
     assembling_time = (kneading_time + resting_time) / 10
     total_time = onion_time + garlic_pepper_time + kneading_time + resting_time + assembling_time
     result = total_time
     
     return result

print(solution())