def solution():
    # Calculate the number of oranges needed by Cassandra
    cassandra_oranges = 2 * 20  

    # Calculate the total number of oranges needed to eat until they are both full
    total_oranges = cassandra_oranges + 20 

    # Calculate the number of oranges remaining after they eat until they are both full
    oranges_remaining = 90 - total_oranges  
    result = oranges_remaining
    return result

print(solution())