import csv



#define functions
def read_dna(dna_filename):
    with open(dna_filename, 'r') as f:
        contents = f.read()
        return contents
    
def dna_length(dna_filename):
    a = read_dna(dna_filename)
    return len(a)

def read_strs(str_filename):
    with open(str_filename) as f:
        list = []
        reader = csv.DictReader(f)
        for row in reader:
            list.append(row)
        return list
    

def get_strs(str_profile):
    if 'name' in str_profile:
        del str_profile['name']
    list = [(k, int(v)) for k, v in str_profile.items()]
    return list

def longest_str_repeat_count(str_frag, dna_seq):
    count = 0
    pattern = str_frag
    while pattern in dna_seq:
        count += 1
        pattern += str_frag
    return count

def find_match(str_profile, dna_seq):
    count_AGAT = longest_str_repeat_count('AGAT', dna_seq)
    count_AATG = longest_str_repeat_count('AATG', dna_seq)
    count_TATC = longest_str_repeat_count('TATC', dna_seq)
    t_AGAT = ('AGAT', count_AGAT)
    t_AATG = ('AATG', count_AATG)
    t_TATC = ('TATC', count_TATC)
    list = [t_AGAT, t_AATG, t_TATC]
    if list == str_profile:
        return True
    else:
        return False

def dna_match(str_filename, dna_filename):
    profiles = read_strs(str_filename)
    dna = read_dna(dna_filename)

    t = 0
    for i in profiles[0:]:
        profile_pick = get_strs(i)
        match = find_match(profile_pick, dna)
        t += 1
        if match:
            if t == 1:
                return 'Alice'
            elif t == 2:
                return 'Bob'
            elif t == 3:
                return 'Charlie'
            elif t == 4:
                return 'No Match'

    



#main conditional
if __name__ == '__main__':

    str_filename = input("Enter STR file: ")
    dna_filename = input("Enter DNA sequence file: ")
    print(dna_match(str_filename, dna_filename))