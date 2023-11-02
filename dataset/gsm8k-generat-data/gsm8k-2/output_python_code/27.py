def solution():
    """Brennan was researching his school project and had to download files from the internet to his computer to use for reference. After downloading 800 files, he deleted 70% of them because they were not helpful. He downloaded 400 more files but again realized that 3/5 of them were irrelevant. How many valuable files was he left with after deleting the unrelated files he downloaded in the second round?"""
    initial_files = 800
    initial_relevant_files = 0.3 * initial_files
    second_download = 400
    second_relevant_files = (2/5) * second_download
    total_relevant_files = initial_relevant_files + second_relevant_files
    result = total_relevant_files
    return result

print(solution())