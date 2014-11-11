import re
import numpy as np
def extract(fname, keyWord):
    f = open(fname)
    cont = f.read()
    f.close()
    instances = cont.strip().split("\n\n")
    instances = [inst for inst in instances if keyWord in inst.split("\n")[1]] 
    K_pattern = re.compile(r"k: (\d+)")
    total_pattern = re.compile(r"total edges: (\d+)")
    covered_pattern = re.compile(r"covred edge: (\d+)")
    dist_pattern = re.compile(r"distriution: \n\d+,(\d+),")
    result = []
    for inst in instances:
        K = K_pattern.search(inst).group(1)
        total = total_pattern.search(inst).group(1)
        cover = covered_pattern.search(inst).group(1)
        dist = dist_pattern.search(inst).group(1)
        result.append([K, total, cover, dist])
    np.savetxt('test.txt', result)     

   
    return result

if __name__ == "__main__":
    extract("topk_size.txt", "data")
