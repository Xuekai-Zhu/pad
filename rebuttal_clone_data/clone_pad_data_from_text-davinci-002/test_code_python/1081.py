def solution():
     hive_1_bees = 1000
     hive_1_honey = 500
     hive_2_bees = hive_1_bees * 0.8
     hive_2_honey = hive_1_honey * 1.4
     total_honey = hive_1_honey + hive_2_honey
 
     return total_honey

print(solution())