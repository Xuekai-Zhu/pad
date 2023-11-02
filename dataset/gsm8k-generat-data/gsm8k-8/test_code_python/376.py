def solution():
    # Define the number of apples that Kayla picked
    kayla_picked = 20

    # Calculate the number of apples Caleb picked
    caleb_picked = kayla_picked - 5

    # Calculate the number of apples Suraya picked
    suraya_picked = caleb_picked + 12

    # Calculate the difference between the number of apples Suraya picked and the number Kayla picked
    difference = suraya_picked - kayla_picked

    result = difference
    return result

print(solution())