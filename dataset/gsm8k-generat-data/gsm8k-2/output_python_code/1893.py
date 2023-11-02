def solution():
    """Charlotte is a dog walker and is creating a schedule for all of her clients this week. Each dog is walked separately. On Monday, she needs to walk 4 poodles and 2 Chihuahuas. On Tuesday, she walks the same amount of Chihuahuas but isn't sure how many poodles she should walk. On Wednesday, she walks 4 Labradors. It takes 2 hours to walk a poodle, 1 hour to walk a Chihuahua, and 3 hours to walk a Labrador. If she has time for a total of 32 hours spent in dog-walking this week, how many poodles can Charlotte walk on Tuesday?"""
    monday_poodles = 4
    monday_chihuahuas = 2
    tuesday_chihuahuas = monday_chihuahuas
    wednesday_labradors = 4
    poodle_time = 2
    chihuahua_time = 1
    labrador_time = 3
    total_time = 32
    remaining_time = total_time - ((monday_poodles * poodle_time) + (monday_chihuahuas * chihuahua_time) + (wednesday_labradors * labrador_time))
    tuesday_poodles = remaining_time // poodle_time
    result = tuesday_poodles
    return result

print(solution())