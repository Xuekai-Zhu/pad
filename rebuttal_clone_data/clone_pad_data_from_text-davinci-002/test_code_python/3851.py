def solution():
     spain_russia = 7019
     spain_germany = 1615
     germany_russia = spain_russia - spain_germany
     total_distance = germany_russia + spain_germany + spain_germany
     result = total_distance
     return result

print(solution())