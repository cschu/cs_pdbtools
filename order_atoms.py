#!/usr/bin/python

'''
Created on Apr 13, 2012

@author: Chris
'''


import sys

ORDER_BY_NA_BACKBONE_IGNORE_BASE = {"P": 0, 
                                    "OP1": 1,
                                    "OP2": 2,
                                    "O5'": 3,
                                    "C5'": 4,
                                    "C4'": 5,
                                    "O4'": 5.5,
                                    "C3'": 6,
                                    "O3'": 7,
                                    "C2'": 8,
                                    "O2'": 8.5,   
                                    "C1'": 9,
                                    "ignore": 10000
                                    }      

"""
ATOM      1  P     G A   1       0.882  -9.772 -61.888  1.00 74.54           P  
ATOM      2  OP1   G A   1       0.790  -8.505 -61.104  1.00 69.34           O  
ATOM      3  OP2   G A   1       1.874  -9.867 -63.004  1.00 75.99           O  
ATOM      4  O5'   G A   1       1.050 -11.024 -60.877  1.00 69.01           O  
ATOM      5  C5'   G A   1       2.311 -11.103 -60.223  1.00 66.43           C  
ATOM      6  C4'   G A   1       2.305 -11.628 -58.794  1.00 63.77           C  
ATOM      7  O4'   G A   1       2.607 -13.051 -58.862  1.00 65.29           O  
ATOM      8  C3'   G A   1       3.429 -11.074 -57.894  1.00 61.34           C  
ATOM      9  O3'   G A   1       3.173  -9.826 -57.174  1.00 58.46           O  
ATOM     10  C2'   G A   1       3.743 -12.225 -56.937  1.00 60.71           C  
ATOM     11  O2'   G A   1       2.905 -12.316 -55.818  1.00 59.53           O  
ATOM     12  C1'   G A   1       3.559 -13.426 -57.857  1.00 62.53           C  
ATOM     13  N9    G A   1       4.878 -13.822 -58.368  1.00 63.85           N  
ATOM     14  C8    G A   1       5.980 -14.069 -57.559  1.00 63.93           C  
ATOM     15  N7    G A   1       7.064 -14.398 -58.213  1.00 65.36           N  
ATOM     16  C5    G A   1       6.640 -14.359 -59.528  1.00 65.36           C  
ATOM     17  C6    G A   1       7.400 -14.624 -60.652  1.00 67.53           C  
ATOM     18  O6    G A   1       8.584 -14.936 -60.635  1.00 69.43           O  
ATOM     19  N1    G A   1       6.655 -14.493 -61.814  1.00 68.58           N  
ATOM     20  C2    G A   1       5.321 -14.136 -61.846  1.00 67.12           C  
ATOM     21  N2    G A   1       4.743 -14.053 -63.053  1.00 68.75           N  
ATOM     22  N3    G A   1       4.585 -13.881 -60.781  1.00 63.32           N  
ATOM     23  C4  
"""

"""
 1 -  6        Record name   "ATOM  "
 7 - 11        Integer       serial       Atom  serial number.
13 - 16        Atom          name         Atom name.
17             Character     altLoc       Alternate location indicator.
18 - 20        Residue name  resName      Residue name.
22             Character     chainID      Chain identifier.
23 - 26        Integer       resSeq       Residue sequence number.
27             AChar         iCode        Code for insertion of residues.
31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
55 - 60        Real(6.2)     occupancy    Occupancy.
61 - 66        Real(6.2)     tempFactor   Temperature  factor.
77 - 78        LString(2)    element      Element symbol, right-justified.
79 - 80        LString(2)    charge       Charge  on the atom.
"""
"""
         1         2         3         4         5         6         7         8 
12345678901234567890123456789012345678901234567890123456789012345678901234567890
ATOM    496  P     G A  24      22.107  19.599 -41.155  1.00 53.10           P  
ATOM    497  OP1   G A  24      22.948  18.440 -41.513  1.00 54.61           O  
ATOM    498  OP2   G A  24      20.932  19.928 -42.008  1.00 50.14           O  
ATOM    499  O5'   G A  24      21.631  19.462 -39.610  1.00 49.70           O  
ATOM    500  C5'   G A  24      22.530  19.726 -38.521  1.00 46.76           C  
ATOM    501  C4'   G A  24      21.843  19.905 -37.172  1.00 43.33           C  
ATOM    502  O4'   G A  24      21.236  21.217 -37.129  1.00 40.92           O  
ATOM    503  C3'   G A  24      20.657  19.038 -36.747  1.00 40.62           C  
ATOM    504  O3'   G A  24      20.970  17.696 -36.341  1.00 42.32           O  
ATOM    505  C2'   G A  24      20.218  19.866 -35.537  1.00 38.62           C  
ATOM    506  O2'   G A  24      21.117  19.817 -34.440  1.00 39.05           O  
ATOM    507  C1'   G A  24      20.178  21.236 -36.180  1.00 35.68           C

ATOM    185  C1'   C     9     -15.196  -3.119 -47.686  1.00 82.84           C 

ATOM    142  C1'   C     7     -13.325   7.581 -38.765  1.00 55.49           C  
ATOM    143  C2    C     7     -11.390   8.568 -40.016  1.00 53.81           C  
"""


ATOM_STR = "%-6s%5i %4s%c%3s %c%4i%c   %8.3f%8.3f%8.3f%6.2f%6.2f          %2s%2s"

def write_atom(atom, out=sys.stdout):
    atomstr = ATOM_STR % ('ATOM',
                          atom['serial'],
                          ' %-3s' % atom['name'],
                          atom['altLoc'],
                          atom['resName'],
                          atom['chainID'],
                          atom['resSeq'],
                          atom['iCode'],
                          atom['x'],
                          atom['y'],
                          atom['z'],
                          atom['occupancy'],
                          atom['tempFactor'],
                          atom['element'],
                          atom['charge'])
    out.write('%s\n' % atomstr)
    pass
    
    

def build_atomdict(line):
    return {'serial': int(line[6:11]),
            'name': line[12:16].strip(),
            'altLoc': line[16],
            'resName': line[17:20].strip(),
            'chainID': line[21],
            'resSeq': int(line[22:26]),
            'iCode': line[26],
            'x': float(line[30:38]),
            'y': float(line[38:46]),
            'z': float(line[46:54]),
            'occupancy': float(line[54:60]),
            'tempFactor': float(line[60:66]),
            'element': line[76:78].strip(),
            'charge': line[78:80].strip()}





def reorder_atoms(resdata, start_index, order=ORDER_BY_NA_BACKBONE_IGNORE_BASE):    
    
    ordered = sorted(resdata, key=lambda x:order.get(x['name'].strip(), order['ignore']))
    # print [atom['name'] for atom in ordered]
    
    for i, atom in enumerate(ordered):        
        atom['serial'] = i + start_index
        write_atom(atom)
    pass




def main(argv):
    
    # Testing @ home    
    # fn = open("c:\\users\\chris\\workspace\\cs_pdbtools\\testcases\\sixhairpin.pdb") 
    # fn = open("c:\\users\\chris\\workspace\\cs_pdbtools\\testcases\\2qba.pdb")
    fn = open(argv[0])    
    
    current_residue = None
    residue_data = []
    current_atom_index = 1
    
    for line in fn:
        # print '**', line        
        if line.startswith('ATOM'):
            atom = build_atomdict(line)
            res_id = (atom['resSeq'], atom['chainID'], atom['iCode'])
            if (current_residue is None) or res_id == current_residue:
                current_residue = res_id
                residue_data.append(atom)
            else:
                reorder_atoms(residue_data, current_atom_index)
                current_atom_index += len(residue_data) 
                current_residue = res_id               
                residue_data = [atom]
                
        else:
            # This case occurs when CONECT lines follow the coordinate section.            
            if residue_data:
                reorder_atoms(residue_data, current_atom_index)
                residue_data = []                
            sys.stdout.write('%s\n' % line.strip())
    
    # Without CONECT lines, this is needed to write the last residue.
    if residue_data:
                reorder_atoms(residue_data, current_atom_index)
    
    
    pass


if __name__ == '__main__': main(sys.argv[1:])