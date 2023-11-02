def solution():
    """Charlotte is a dog walker and is creating a schedule for all of her clients this week. Each dog is walked separately. On Monday, she needs to walk 4 poodles and 2 Chihuahuas. On Tuesday, she walks the same amount of Chihuahuas but isn't sure how many poodles she should walk. On Wednesday, she walks 4 Labradors. It takes 2 hours to walk a poodle, 1 hour to walk a Chihuahua, and 3 hours to walk a Labrador. If she has time for a total of 32 hours spent in dog-walking this week, how many poodles can Charlotte walk on Tuesday?"""
    # Define the time required to walk each type of dog
    POODLE_TIME = 2
    CHIHUAHUA_TIME = 1
    LABRADOR_TIME = 3

    # Define the number of dogs to walk on each day
    monday_poodles = 4
    monday_chihuahuas = 2
    tuesday_chihuahuas = monday_chihuahuas
    wednesday_labradors = 4

    # Calculate the total time spent on each type of dog
    poodle_time = monday_poodles * POODLE_TIME
    chihuahua_time = monday_chihuahuas * CHIHUAHUA_TIME + tuesday_chihuahuas * CHIHUAHUA_TIME
    labrador_time = wednesday_labradors * LABRADOR_TIME

    # Calculate the total time spent walking dogs
    total_time = poodle_time + chihuahua_time + labrador_time

    # Calculate how many poodles can be walked on Tuesday
    poodles_allowed = (32 - total_time) // POODLE_TIME

    # Display the number of poodles Charlotte can walk on Tuesday
    result = poodles_allowed
    return result

print(solution())