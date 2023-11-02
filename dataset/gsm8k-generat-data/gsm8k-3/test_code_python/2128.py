def solution():
    """A jug needs 40 cups of water to be full. A custodian at Truman Elementary School has to fill water jugs for 200 students, who drink 10 cups of water in a day. How many water jugs will the custodian fill with cups of water to provide the students with all the water they need in a day?"""
    # Define the number of cups of water the students need in a day
    cups_per_student = 10
    total_cups = cups_per_student * 200

    # Calculate the number of jugs needed to hold all the water
    jugs_needed = total_cups / 40

    # Round up to the nearest integer
    jugs_needed = int(jugs_needed) + (jugs_needed % 1 > 0)

    # Display the number of jugs needed
    result = jugs_needed
    return result

print(solution())