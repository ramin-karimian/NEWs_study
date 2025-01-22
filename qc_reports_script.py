import os

def exe_cmd(cmd):
    print(f"executing : \n{cmd}")
    os.system(cmd)
    print("\n\n")

if __name__=="__main__":

    threads = 40
    data_folder = f'/arc/project/st-spakpour-1/news_project_data/'

    fastqc_folder = f'outputs/qc_results/fastqc'
    multiqc_folder = f'outputs/qc_results/multiqc'


    if f'fastqc' not in os.listdir("outputs/qc_results"):
        os.mkdir(fastqc_folder)
        os.mkdir(multiqc_folder)

    print('\n\n\nFastQC step\n')
    cmd1 = f"fastqc -f fastq -o {fastqc_folder} {data_folder}/*.fastq.gz -t {threads} > Slurm_scripts/logfiles/{fastqc_folder.split('/')[-1]}.log 2>&1 "
    exe_cmd(cmd1)

    print('\n\n\nMultiQC step\n')
    cmd2 = f"multiqc {fastqc_folder} -o {multiqc_folder}"
    exe_cmd(cmd2)


