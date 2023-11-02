def solution():
     oranges = 3
     juices = 7
     honey = 3
     plants = 4

     cost_oranges = oranges * 4.50
     cost_juices = juices * 0.50
     cost_honey = honey * 5
     cost_plants = plants * 18 / 2

     total_cost = cost_oranges + cost_juices + cost_honey + cost_plants

     result = total_cost
     return result

print(solution())