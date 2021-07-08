from ete3 import PhyloTree

from skbio import DistanceMatrix
from skbio.tree import nj

def inicio(d1, d2, d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16):
    print("Tree using only a distance matrix")
    data = [[d1, d2, d3, d4],
            [d5, d6, d7, d8],
            [d9, d10, d11, d12],         
            [d13, d14, d15, d16]]

    '''data = [[0,     0.4,    0.35,   0.6],
            [0.4,   0,      0.45,   0.7],
            [0.35,  0.45,   0,      0.55],         
            [0.6,   0.7,    0.55,   0]]        
        '''
    ids = list('ABCD')
    dm = DistanceMatrix(data, ids)
    tree = nj(dm)
    print(tree.ascii_art())
    newick_str = nj(dm, result_constructor=str)
    print(newick_str)
    #print(newick_str[:55], "...")
    t = PhyloTree(newick_str)
    t.render("mytree2.png", w=183, units="mm")
    #t.show()

d1 = 0
d2 = 0.4
d3 = 0.35
d4 = 0.6
d5 = 0.4
d6 = 0
d7 = 0.45
d8 = 0.7
d9 = 0.35
d10 = 0.45
d11 = 0
d12 = 0.55
d13 = 0.6
d14 = 0.7
d15 = 0.55
d16 = 0

if __name__ == "__main__":
    
    inicio(d1, d2, d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16)
   