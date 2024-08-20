# vcf-parser
A small vcf parser I made for an intership project.

The parser aim is to read through a vcf file and create csv version of it with SNP, no NA containing lines, and only SNPs with exactly one mutation (0 or 1)

# Options

The parser is also able to return only the SNP present on a specific chromosome (scaffold; you need to give a scaffold name for the "-sc" option)

By default the outfile is called "parsed.csv" or "parsed_*scaf*.csv". And is located in a folder called "./csv/" that you need to create in the same folder as you have the parser. You can change the name of you outfile by using the option "-o".

The infile is given in the "-i" option (It won't work without it).
