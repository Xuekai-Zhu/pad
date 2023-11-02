def solution():
    """Aston has accidentally torn apart his comics and needs to put all the pages back together. Each comic has 25 pages and Aston has found 150 pages on the floor. He puts his comics back together and adds them back into his box of comics. If there were already 5 untorn comics in the box, how many comics are now in the box of comics?"""
    pages_per_comic = 25
    torn_pages = 150
    total_pages = torn_pages + pages_per_comic * (5 + x) # x is the number of comics added
    comics_total = total_pages // pages_per_comic
    result = comics_total
    return result

print(solution())