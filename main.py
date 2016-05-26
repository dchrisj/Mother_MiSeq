import os
from subprocess import call
from stability import create_stab_file
from summary import parse_summary
from summary import summary_stats

def run_cmd(cmds):
    command = ' '.join(cmds)
    os.system(command)

def wrap():
    def create_stability():
        create_stab_file()

    def make_contigs():
        commands = ['mothur', '"#make.contigs(file=stability.files, processors=8)"']
        run_cmd(commands)

    def summary_seqs():
        commands = ['mothur', '"#summary.seqs(fasta=stability.trim.contigs.fasta)"']
        run_cmd(commands)

    def screen_seqs():
        records = parse_summary("stability.trim.contigs.summary")
        ambigs, nbases = summary_stats(records)
        print "HERE" + str(ambigs) + ' ' + str(nbases)
        commands = ['mothur', '"#screen.seqs(fasta=stability.trim.contigs.fasta, group=stability.contigs.groups, maxambig=' + str(ambigs) + ', maxlength=' + str(nbases) + ')"']
        run_cmd(commands)

    def pipeline():
        create_stability()
        make_contigs()
        summary_seqs()
        screen_seqs()

    pipeline()

if __name__ == "__main__":
    wrap()
