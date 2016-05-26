import csv
import math

class SummarySeq(object):
    def __init__(self, name, start, end, nbases, ambigs, polymer, num_seqs):
        self.name = name
        self.start = start
        self.end = end
        self.nbases = nbases
        self.ambigs = ambigs
        self.polymer = polymer
        self.num_seqs = num_seqs

def summary_stats(records):
    ambigs = nbases = 0.0
    count = len(records)
    for rec in records:
        ambigs += rec.ambigs
        nbases += rec.nbases
    ambigs /= count
    nbases /= count
    return int(math.ceil(ambigs)), int(math.ceil(nbases))

def parse_summary(fname):
    records = []
    with open(fname, 'r') as fp:
        header = fp.readline().strip()
        while 2 != 1:
            record = fp.readline().strip().split("\t")
            if len(record) > 3:
                name, start, end, nbases, ambigs, polymer, num_seqs = record
                records.append(SummarySeq(name, int(start), int(end), int(nbases), int(ambigs), polymer, int(num_seqs)))
            else:
                break
    fp.close()
    return records    

if __name__ == "__main__":
    pass
    """
    records = parse_summary('stability.trim.contigs.summary')
    a, b = summary_stats(records)
    print a, b
    """
