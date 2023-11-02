def solution():
     sandcastles_on_Mark's_beach = 20
     towers_on_Mark's_beach = sandcastles_on_Mark's_beach * 10
     sandcastles_on_Jeff's_beach = sandcastles_on_Mark's_beach * 3
     towers_on_Jeff's_beach = sandcastles_on_Jeff's_beach * 5
     total_sandcastles = sandcastles_on_Mark's_beach + sandcastles_on_Jeff's_beach
     total_towers = towers_on_Mark's_beach + towers_on_Jeff's_beach
     return (total_sandcastles, total_towers)

print(solution())