import csv
import os
import argparse

def parser(infile, outfile = "csv/parsed.csv", scaf = None) :
    if scaf != None and outfile == "csv/parsed.csv" :  
        outfile = "csv/parsed_" + scaf + ".csv"
    if os.path.exists(outfile) : #First, we check that the outfile name/directory aint already taken.
        os.remove(outfile)
    nucl_lib = ['A', 'T', 'C', 'G']
    with open(infile, "r") as fileopen : 
        for line in fileopen : 
            if line[0:2] != "##":
                if line[0] == "#" : 
                    header = line.split()
                    del header[2]
                    del header[4:8]
                    with open(outfile, 'a') as csv_out :  #And we add our header in our .csv.
                        write_out = csv.writer(csv_out)
                        write_out.writerow(header)
                else : 
                    if scaf == None :
                        line_spl = line.split()
                        if (line_spl[3] in nucl_lib) and (line_spl[4] in nucl_lib) : 
                            line_fin = line_spl
                            for i in range(len(line_spl)) : 
                                if i > 8 : 
                                    if line_spl[i][0] != '.' :
                                        line_fin[i] = line_spl[i][0]
                                    else : 
                                        line_fin[i] = 'NA'
                            del line_fin[2]
                            del line_fin[4:8]
                            with open(outfile, 'a') as csv_out :  #And we add our line in our .csv.
                                write_out = csv.writer(csv_out)
                                write_out.writerow(line_spl)
                    else : 
                        line_spl = line.split()
                        if line_spl[0] == scaf : 
                            if (line_spl[3] in nucl_lib) and (line_spl[4] in nucl_lib) : 
                                line_fin = line_spl
                                for i in range(len(line_spl)) : 
                                    if i > 8 : 
                                        if line_spl[i][0] != '.' :
                                            line_fin[i] = line_spl[i][0]
                                        else : 
                                            line_fin[i] = 'NA'
                                del line_fin[2]
                                del line_fin[4:8]
                                with open(outfile, 'a') as csv_out :  #And we add our line in our .csv.
                                    write_out = csv.writer(csv_out)
                                    write_out.writerow(line_spl) 





if __name__ == "__main__" :
    arg_manager = argparse.ArgumentParser() #Here we parse the arguments of our script. 
    arg_manager.add_argument('-infile', '-i', type = str)
    arg_manager.add_argument('-scaf', '-sc', type = str)
    arg_manager.add_argument('-outfile', '-o', type = str)
    args = arg_manager.parse_args()
    if args.scaf : 
        parser(args.infile, scaf = args.scaf)
    elif args.outfile : 
        parser(args.infile, args.outfile)
    else : 
        parser(args.infile)
