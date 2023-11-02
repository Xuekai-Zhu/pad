def solution():
    """Brennan was researching his school project and had to download files from the internet to his computer to use for reference. After downloading 800 files, he deleted 70% of them because they were not helpful. He downloaded 400 more files but again realized that 3/5 of them were irrelevant. How many valuable files was he left with after deleting the unrelated files he downloaded in the second round?"""
    initial_files = 800
    percentage_deleted = 70
    remaining_files = initial_files * (100 - percentage_deleted) / 100
    second_round_files = 400
    irrelevant_percentage = 3/5
    relevant_files = second_round_files * (1 - irrelevant_percentage)
    total_valuable_files = remaining_files + relevant_files
    result = total_valuable_files
    return result

print(solution())