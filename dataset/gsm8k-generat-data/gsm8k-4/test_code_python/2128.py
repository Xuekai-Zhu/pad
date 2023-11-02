def solution():
    """A jug needs 40 cups of water to be full. A custodian at Truman Elementary School has to fill water jugs for 200 students, who drink 10 cups of water in a day. How many water jugs will the custodian fill with cups of water to provide the students with all the water they need in a day?"""
    # Define the number of cups of water needed for each student
    cups_per_student = 10

    # Define the total number of cups of water needed for all students
    total_cups = cups_per_student * 200

    # Calculate the number of jugs required to fill the required cups of water
    jugs = total_cups / 40
    jugs = round(jugs + 0.5) # round up to nearest integer

    result = jugs
    return result

print(solution())