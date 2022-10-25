from ctypes.wintypes import CHAR
import math
import re
import pandas


# CLASSE ATOM PDB

class AtomPDB:
    def __init__(self, card, atom_id, atom_type, amm_code, chain_id, residue_id, x, y, z, occ, disp, element):
        self.card = card
        self.atom_id = atom_id  # atom progressive id
        self.atom_type = atom_type
        self.amm_code = amm_code  # three letters' code of amino acid
        self.chain_id = chain_id
        self.residue_id = residue_id
        self.x = x
        self.y = y
        self.z = z
        self.occ = occ  # atom occupancy
        self.disp = disp  # atom displacement
        self.element = element

    def __init__(self, atom):
        self.card = atom[0]
        self.atom_id = int(atom[1])
        self.atom_type = atom[2]
        self.amm_code = atom[3]
        self.chain_id = atom[4]
        self.residue_id = atom[5]
        self.x = float(atom[6])
        self.y = float(atom[7])
        self.z = float(atom[8])
        self.occ = float(atom[9])
        self.disp = float(atom[10])
        self.element = atom[11]

    def print_atom_pdb(self):
        print("Label: " + self.card)
        print("Atom ID: " + str(self.atom_id))
        print("Atom type: " + self.atom_type)
        print("Residue: " + self.amm_code)
        print("Residue ID: " + str(self.residue_id))
        print("Chain ID: " + self.chain_id)
        print("X: " + str(self.x))
        print("Y: " + str(self.y))
        print("Z: " + str(self.z))
        print("Occupancy: " + str(self.occ))
        print("Displacement: " + str(self.disp))
        print("Element: " + self.element)


class AtomDistance:
    def __init__(self, atm_id1, atm1, res1, res_id1, chain1, atm_id2, atm2, res2, res_id2, chain2, distance):
        self.atm_id1 = atm_id1
        self.atm1 = atm1
        self.res1 = res1
        self.res_id1 = res_id1
        self.chain1 = chain1
        self.atm_id2 = atm_id2
        self.atm2 = atm2
        self.res2 = res2
        self.res_id2 = res_id2
        self.chain2 = chain2
        self.distance = distance

    def print_atom_distance(self):
        print("First Atom id: " + str(self.atm_id1))
        print("First Atom type: " + self.atm1)
        print("First Residue: " + self.res1)
        print("First Residue ID: " + str(self.res_id1))
        print("First Chain: " + self.chain1)
        print("Second Atom id: " + str(self.atm_id2))
        print("Second Atom type: " + self.atm2)
        print("Second Residue: " + self.res2)
        print("Second Residue ID: " + str(self.res_id2))
        print("Second Chain: " + self.chain2)
        print("Distance: " + str(self.distance))

    def writefile_distance(self, xs):
        xs.write("First Atom id: " + str(self.atm_id1) + "\n")
        xs.write("First Atom type: " + self.atm1 + "\n")
        xs.write("First Residue: " + self.res1 + "\n")
        xs.write("First Residue ID: " + str(self.res_id1) + "\n")
        xs.write("First Chain: " + self.chain1 + "\n")
        xs.write("Second Atom id: " + str(self.atm_id2) + "\n")
        xs.write("Second Atom type: " + self.atm2 + "\n")
        xs.write("Second Residue: " + self.res2 + "\n")
        xs.write("Second Residue ID: " + str(self.res_id2) + "\n")
        xs.write("Second Chain: " + self.chain2 + "\n")
        xs.write("Distance: " + str(self.distance) + "\n")

    def create_csv(self, csv):
        csv.write(str(self.atm_id1) + ";")
        csv.write((self.atm1) + ";")
        csv.write((self.res1) + ";")
        csv.write(str(self.res_id1) + ";")
        csv.write((self.chain1) + ";")
        csv.write(str(self.atm_id2) + ";")
        csv.write((self.atm2) + ";")
        csv.write((self.res2) + ";")
        csv.write(str(self.res_id2) + ";")
        csv.write((self.chain2) + ";")
        csv.write(str(self.distance))



def atom_distance(x1, x2, y1, y2, z1, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def atom_split(atm):
    
    f_atm = []
    
    
    f_atm.append(atm[0:6])
    #f_atm[0].strip()
    f_atm.append(atm[6:11])
    #f_atm[1]
    f_atm.append(atm[12:16])
    #f_atm[2].strip()
    f_atm.append(atm[16:20])
    #f_atm[3].strip()
    f_atm.append(atm[21])
    #f_atm[4].strip()
    f_atm.append(atm[22:26])
    #f_atm[5].strip()
    f_atm.append(atm[30:38])
    #f_atm[6].strip()
    f_atm.append(atm[38:46])
    #f_atm[7].strip()
    f_atm.append(atm[46:54])
    #f_atm[8].strip()
    f_atm.append(atm[54:60])
    #f_atm[9].strip()
    f_atm.append(atm[60:66])
    #f_atm[10].strip()
    f_atm.append(atm[76:78])
    #f_atm[11].strip()

    return f_atm




atm_list = []  # lista atomi
atom_chain1 = []
atom_chain2 = []
choice = True
firstChains = []
secondChains = []


print("---LISTA DISTANZE TRA ATOMI---\n")
print("Please insert the filename: ")
filename = input()  # inserisci file

first_chain = input("Insert the first chain ID: ")
firstChains.append(first_chain)
while choice:
    print("Do you want to add another chain? Y/N\n")
    answer = input()
    if answer == "Y":
        newFirstChain: CHAR = input("Insert another chain: ")
        firstChains.append(newFirstChain)
    else:
        choice = False    

sec_chain = input("Insert the second chain ID: ")
choice = True
secondChains.append(sec_chain)
while choice:
    print("Do you want to add another chain? Y/N\n")
    answer = input()
    if answer == "Y":
        newSecChain: CHAR = input("Insert another chain: ")
        firstChains.append(newSecChain)
    else:
        choice = False 


with open(filename, "r") as file:
    lines = file.readlines()

for line in lines:  # scompatta il file estraendo tutte le righe che iniziano con ATOM
    if re.match("ATOM", line):
        f_atm = atom_split(line)
        atm_list.append(f_atm)


# for atm in atm_list:
#    print(atm)       

for atm in atm_list:  # crea i due oggetti- lista che corrispondono aglia tomi della catena corrisp.
    for fchain in firstChains:
        if fchain == atm[4]:
            atom_chain1.append(atm)

for atm in atm_list:
    for schain in secondChains:
        if schain == atm[4]:
            atom_chain2.append(atm)


def create_residue(atom_list, t_res, id_res):  # CREA UN RES COME LISTA DI ATOMI
    res = []
    for atom in atom_list:
        if (t_res == atom[3]) and (id_res == atom[5]):
            res.append(atom)
    return res


def create_res_list(atom_list):  # CREA UNA CATENA COME LISTA DI RESIDUI
    res_list = []
    for atom in atom_list:
        res = create_residue(atom_list, atom[3], atom[5])
        if not (res_list.__contains__(res)):
            res_list.append(res)
    return res_list


res_list_1 = create_res_list(atom_chain1)
res_list_2 = create_res_list(atom_chain2)


i1 = 0  # indici di ciclo
i2 = 0
dist = []
arr_m_dist = []
obj_distanze = []

def min_res_dist(res1, res2, obj_dist, arr_m_dist):
    arr_dist = []
    mom_obj_dist = []
    for atm1 in res1:
        for atm2 in res2:
            dis = atom_distance(float(atm1[6]), float(atm2[6]), float(atm1[7]), float(atm2[7]), float(atm1[8]),
                                float(atm2[8]))
            arr_dist.append(dis)
            aqu = AtomDistance(atm1[1], atm1[2], atm1[3], atm1[5], atm1[4], atm2[1], atm2[2], atm2[3], atm2[5], atm2[4],
                             dis)
            mom_obj_dist.append(aqu)
    qu = min(arr_dist)
    if 3 <= qu <= 5:
        arr_m_dist.append(qu)
        for al in mom_obj_dist:
            if al.distance == qu:
                obj_dist.append(al)


for t in res_list_1:  # calcolo delle distanze tra le due catene e creazione oggetti distanze
    for a in res_list_2:
        min_res_dist(t, a, obj_distanze, arr_m_dist)

print(len(arr_m_dist))
print("------")
for ar in arr_m_dist:
    print(ar)

i = 1

t = open("Distances.txt", "w")

for q in obj_distanze:
    q.writefile_distance(t)
    t.write("\n")
    i = i + 1
t.close()
ab = open("Distances.txt", "r")
s = "Distance"
x = 0
for word in ab:
    if re.search(s, word):
        x = x + 1
ab.close()
print(x)

csv = open("distanze.csv", "w")
csv.write("First Atom id;First Atom type;First Residue;First Residue ID;First Chain;Second Atom id;" +
    "Second Atom type;Second Residue;Second Residue ID;Second Chain;Distance" + "\n")
for q in obj_distanze:
    q.create_csv(csv)
    csv.write("\n")
    i = i + 1
csv.close()

df = pandas.read_csv('distanze.csv', sep=';')
print(df)