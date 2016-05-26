import os
import sys

def ld(s, t):
    if s == t:
        return 0
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)

    v0 = range(len(t)+1)
    v1 = range(len(t)+1)
    
    for i in range(len(v0)):
        v0[i] = i
        
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            if s[i] == t[j]:
                cost = 0
            else:
                cost = 1
            v1[j+1] = min(v1[j] + 1, v0[j+1] + 1, v0[j] + cost)
        for k in range(len(v0)):
            v0[k] = v1[k]
    return v1[len(t)]

def get_fastq_files():
    cwd = os.getcwd()
    fq_files = []
    for f in os.listdir(cwd):
        if f.endswith(".fastq") or f.endswith(".fq"):
            fq_files.append(f)
    return fq_files

def get_fastq_abbr(fq_files):
    fastq_abbr = ""
    st = [".", "_", "/", "-"]
    prefix_idx = min(fq_files.find(i) for i in st if i in fq_file)
    fastq_abbr = (fq_file[0:prefix_idx])
    return fastq_abbr

def stab_file_triplet():
    fq_files = get_fastq_files()
    cost = sys.maxint
    best_match = ""
    visited = res = []
    for fq_file in fq_files:
        curr = fq_file
        if curr not in visited:
            visited.append(curr)
            for f in fq_files:
                if curr == f or f in visited:
                    pass
                else:
                    curr_cost = ld(curr, f)
                    if curr_cost < cost:
                        cost = curr_cost
                        best_match = f
            visited.append(best_match)
            cost = sys.maxint
            abbr = get_fastq_abbr(curr)
            res.append( [abbr, curr, best_match] )
    return res

def create_stab_file():
        with open("stability.files", "w") as fp:
            fq_triplet = stability_file_triplet()
            for triplet in fq_triplet:
                for attr in triplet:
                    fp.write(attr, + "\t")
                fp.write("\n")
        fp.close()

if __name__ == "__main__":
    pass
