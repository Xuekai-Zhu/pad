def solution():
    """Aston has accidentally torn apart his comics and needs to put all the pages back together. Each comic has 25 pages and Aston has found 150 pages on the floor. He puts his comics back together and adds them back into his box of comics. If there were already 5 untorn comics in the box, how many comics are now in the box of comics?"""
    
    # Calculate the total number of torn comics
    torn_comics = 150 // 25
    
    # Calculate the total number of comics in the box
    total_comics = torn_comics + 5
    
    result = total_comics
    return result

print(solution())