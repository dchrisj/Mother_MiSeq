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
        commands = ['mothur', '"#screen.seqs(fasta=stability.trim.contigs.fasta, group=stability.contigs.groups, maxambig=' + str(ambigs) + ', maxlength=' + str(nbases) + ')"']
        run_cmd(commands)

    def unique_seqs():
        commands = ['mothur', '"#unique.seqs(fasta=stability.trim.contigs.good.fasta)"']
        run_cmd(commands)

    def count_seqs():
        commands = ['mothur', '"#count.seqs(name=stability.trim.contigs.good.names, group=stability.contigs.good.groups)"']
        run_cmd(commands)

    def summary_seqs_count():
        commands = ['mothur', '"#summary.seqs(fasta=stability.trim.contigs.good.unique.fasta, count=stability.trim.contigs.good.count_table)"']
        run_cmd(commands)

    def pcr_seqs():
        commands = ['mothur', '"#pcr.seqs(fasta=silva.bacteria.fasta, start=11894, end=25319, keepdots=F, processors=8)"']
        run_cmd(commands)

    def system():
        commands = ['mothur', '"#system(mv silva.bacteria.pcr.fasta silva.v4.fasta)"']
        run_cmd(commands)

    def align():
        commands = ['mothur', '"#align.seqs(fasta=stability.trim.contigs.good.unique.fasta, reference=silva.v4.fasta)"']
        run_cmd(commands)

    def summary_seqs_align():
        commands = ['mothur', '"#summary.seqs(fasta=stability.trim.contigs.good.unique.align, count=stability.trim.contigs.good.count_table)"']
        run_cmd(commands)

    def pipeline():
        create_stability()
        make_contigs()
        summary_seqs()
        screen_seqs()
        unique_seqs()
        count_seqs()
        summary_seqs_count()
        pcr_seqs()
        system()
        align()
        summary_seqs_align()
         

    pipeline()

if __name__ == "__main__":
    wrap()
    pass
