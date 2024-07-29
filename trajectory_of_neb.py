import sys
import argparse
import matplotlib.pyplot as plt
import os
import re

def process_file(input_file, output_file,energy_list):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        last_occurrence = -1
        last_energy = None
        energy_pattern = re.compile(r'E =\s*(-?\d+\.\d+)')
        for i, line in enumerate(lines):
            if 'i =' in line:
                last_occurrence = i
                match = energy_pattern.search(line)
                if match:
                    last_energy = match.group(1)
        
        if last_occurrence != -1:
            start_line = max(0, last_occurrence - 1)
            with open(output_file, 'a') as f:
                f.writelines(lines[start_line:])
                if last_energy is not None:
                    #f.write(f"Extracted energy: {last_energy}\n")
                    energy_list.append(float(last_energy))

    except FileNotFoundError:
        print(f"File {input_file} not found.")

def print_help():
    help_text = """
    Usage: python extract_lines.py <output_file> <common_prefix> <common_suffix> <start> <end>
    
     Arguments:
        -o, --output OUTPUT_FILE    Name of the output file where the results will be appended. Default is 'neb_trajectory.xyz'.
        -P, --prefix COMMON_PREFIX  Common prefix of the input filenames. Default is 'SiO2-r-0-pos-Replica_nr_'.
        -S, --suffix COMMON_SUFFIX  Common suffix of the input filenames. Default is '-1.xyz'.
        -s, --start START           Starting number in the range of filenames. Default is 1.
        -e, --end END               Ending number in the range of filenames. Default is 7.
    
    Example:
        python extract_lines.py --output output.txt --prefix data --suffix .txt --start 1 --end 5
        This will process files named data1.txt, data2.txt, data3.txt, data4.txt, data5.txt.
    """
    print(help_text)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process files and extract lines based on the last occurrence of "i =".')
    
    parser.add_argument('-o', '--output', type=str, default='neb_trajectory.xyz', help='Name of the output file where the results will be appended. Default is "neb_trajectory.xyz".')
    parser.add_argument('-P', '--prefix', type=str, default='SiO2-r-0-pos-Replica_nr_', help='Common prefix of the input filenames. Default is "SiO2-r-0-pos-Replica_nr_".')
    parser.add_argument('-S', '--suffix', type=str, default='-1.xyz', help='Common suffix of the input filenames. Default is "-1.xyz".')
    parser.add_argument('-s', '--start', type=int, default=1, help='Starting number in the range of filenames. Default is 1.')
    parser.add_argument('-e', '--end', type=int, default=7, help='Ending number in the range of filenames. Default is 7.')

    args = parser.parse_args()

    output_file = args.output
    common_prefix = args.prefix
    common_suffix = args.suffix
    start = args.start
    end = args.end
    cwd = os.getcwd()

    # Clear the output file
    open(output_file, 'w').close()
    energy_list=[]
    for i in range(start, end + 1):
        input_file = f"{common_prefix}{i}{common_suffix}"
        process_file(input_file, output_file,energy_list)
    
    energy_list=[e*27.2113838565563 for e in energy_list]
    e1=energy_list[0]
    energy_list=[e-e1 for e in energy_list]
    plt.figure()
    x=range(start, end + 1)
    plt.plot(x,energy_list,linestyle='--', marker='o')
    plt.title('NEB trajectory energy')
    plt.savefig(cwd+'/neb_energy.png',dpi=400)
    


'''
if __name__ == "__main__":
    if sys.argv[1] in ("--help", "-h"):
        print_help()
        sys.exit(0)

    if len(sys.argv) < 2:
        print("Usage: python extract_lines.py <common_prefix> <start> <end>")
        sys.exit(1)
    
    output_file = 'neb_trajectory.xyz'
    common_suffix = '-1.xyz'

    common_prefix = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    
    # Clear the output file
    open(output_file, 'w').close()
    
    for i in range(start, end + 1):
        input_file = f"{common_prefix}{i}{common_suffix}"
        process_file(input_file, output_file)
        '''