# NEB-analysis
Quick python code to plot NEB trajectory and energies from CP2K outputs

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
  
