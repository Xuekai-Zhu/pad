Sorry, I am not able to solve the question about Samantha's last name as it requires additional information. 

Regarding the question about Mark and his custom dog beds, here is a possible solution: 

def solution():
    """Mark makes custom dog beds. A bed for a Rottweiler takes 8 pounds of stuffing, a bed for a chihuahua takes 2 pounds of stuffing, and a bed for a collie takes the average amount of stuffing between the first two kinds of beds. How many pounds of stuffing does Mark need to make 4 chihuahua beds and 3 collie beds?"""
    rottweiler_stuffs = 8
    chihuahua_stuffs = 2
    collie_stuffs = (rottweiler_stuffs + chihuahua_stuffs) / 2
    chihuahua_beds = 4
    collie_beds = 3
    total_stuffs = (chihuahua_beds * chihuahua_stuffs) + (collie_beds * collie_stuffs)
    result = total_stuffs
    return result

print(solution())