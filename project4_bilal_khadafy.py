dict1={'I':'A','T':'B','R':'C','A':'D','N':'E','S': 'F'
      , 'L': 'G', 'O': 'H', 'M': 'I', 'W':'J', 'U': 'K'
      , 'K': 'L', 'E': 'M', 'H': 'N', 'B': 'O', 'C': 'P'
      ,'D': 'Q', 'F':'R','G':'S','J':'T','P':'U','Q':'V'
      ,'V':'W','X':'x','Y':'y','Z':'z'}
#using subsitution to link all values in input string to values in alphabet
def substitution(string):
    alphabet='abcdefghijklmnopqrstuvwyxz'
    string1=string.replace(" ","")
    lister=list(string1)
    alpha=list(alphabet)
    dict2={lister[i]:alpha[i] for i in range(len(alpha))}
    print(dict2)
#switches the values and the keys in a given dictionary
def opposite(a_dict):
    new_dict={}
    for k,v in dict1.items():
        new_dict[v]=k
    return new_dict
#encrypts a given text file and write the encrypted document into another text file
def encryt(file_in,file_out):
    dict1={'I':'A','T':'B','R':'C','A':'D','N':'E','S': 'F'
      , 'L': 'G', 'O': 'H', 'M': 'I', 'W':'J', 'U': 'K'
      , 'K': 'L', 'E': 'M', 'H': 'N', 'B': 'O', 'C': 'P'
      ,'D': 'Q', 'F':'R','G':'S','J':'T','P':'U','Q':'V'
      ,'V':'W','X':'x','Y':'y','Z':'z'}
    with open(file_in,'r') as f:
        with open(file_out,'w') as out:
            for line in f:
               for ch in line:
                    if ch in dict1:
                       out.write(dict1[ch])
                    else:
                        out.write(ch)
#takes an encrypted text file and decrypts it and writes the decrytped file into another text file                        
def decrypt(filein,key,outputfile):
    w=opposite(key)
    with open(filein,'r') as in1:
        with open(outputfile,'w') as out:
            for line in in1:
                for ch in line:
                    if ch in w:
                        out.write(w[ch])
                    else:
                        out.write(ch)
                    
                       

        
