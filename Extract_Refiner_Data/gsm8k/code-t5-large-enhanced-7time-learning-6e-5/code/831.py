def solution():
    
    # Define the number of kangaroos and the time it takes to travel across a highway
    num_kangaroos = 3
    time_highway = 18

    # Define the speed of each kangaroo
    kangaroo_speed = 0.5

    # Calculate the total time it will take to travel all the kangaroos
    total_kangaroo_time = num_kangaroos * time_highway / kangaroo_speed

    # Calculate the time it will take to travel each turtle
    turtle_time = 4 * (kangaroo_speed / 2)

    # Calculate the total time it will take to travel all the turtles
    total_turtle_time = turtle_time * 4

    # Display the total time it will take to travel all the turtles
    result = total_turtle_time
    return result

print(solution())