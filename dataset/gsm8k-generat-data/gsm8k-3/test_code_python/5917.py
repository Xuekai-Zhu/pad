def solution():
    """Harly's animal shelter has 80 dogs. She adopts out 40% of them but then has to take back 5 because of personality conflicts with other dogs in their adopted homes. How many dogs does she have now?"""
    # Define the initial number of dogs
    initial_dogs = 80

    # Calculate the number of dogs adopted out
    adopted_out = int(initial_dogs * 0.4)

    # Calculate the number of dogs taken back
    taken_back = 5

    # Calculate the current number of dogs
    current_dogs = initial_dogs - adopted_out + taken_back

    # Display the current number of dogs
    result = current_dogs
    return result

print(solution())