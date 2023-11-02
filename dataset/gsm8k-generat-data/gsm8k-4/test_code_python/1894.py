def solution():
    """Charlotte is a dog walker and is creating a schedule for all of her clients this week. Each dog is walked separately. On Monday, she needs to walk 4 poodles and 2 Chihuahuas. On Tuesday, she walks the same amount of Chihuahuas but isn't sure how many poodles she should walk. On Wednesday, she walks 4 Labradors. It takes 2 hours to walk a poodle, 1 hour to walk a Chihuahua, and 3 hours to walk a Labrador. If she has time for a total of 32 hours spent in dog-walking this week, how many poodles can Charlotte walk on Tuesday?"""
    # Define the time it takes to walk each type of dog
    poodle_time = 2
    chihuahua_time = 1
    labrador_time = 3

    # Define the number of each type of dog walked on Monday and Wednesday
    monday_poodles = 4
    monday_chihuahuas = 2
    wednesday_labradors = 4

    # Calculate the total time spent on Monday and Wednesday
    total_time = (monday_poodles * poodle_time) + (monday_chihuahuas * chihuahua_time) + (wednesday_labradors * labrador_time)

    # Calculate the remaining time for Tuesday
    remaining_time = 32 - total_time

    # Calculate the number of Chihuahuas walked on Tuesday
    tuesday_chihuahuas = monday_chihuahuas

    # Calculate the number of Poodles that can be walked on Tuesday
    tuesday_poodles = remaining_time / poodle_time

    result = int(tuesday_poodles)
    return result

print(solution())