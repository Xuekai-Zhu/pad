def solution():
    # Define the cost of one rose and Hanna's budget
    rose_cost = 2
    hanna_budget = 300

    # Calculate the maximum number of roses Hanna can buy
    max_roses = hanna_budget // rose_cost

    # Calculate the number of roses for Jenna and Imma
    jenna_roses = max_roses // 3
    imma_roses = max_roses // 2

    # Calculate the total number of roses given to friends
    total_roses = jenna_roses + imma_roses

    result = total_roses
    return result

print(solution())