import sys

word_dict = {}
origin = {}


def change_array( prefix, array ):
    ret = []
    if array.strip() == "":
        return []
    for w in array.split('\002'):
        ret.append(prefix+w)
    return ret

words = {}

for line in sys.stdin:
    sku, cid3,pw,aw,bw,ew,price,log_price = line.strip().split('\t')
    output = change_array('pw',pw) + change_array('brand',bw) + change_array('adj',aw) + change_array('exp',ew)
    for word in output:
        if word not in origin:
            origin[word] = 1
        origin[word]+=1

for word, n in origin.items():
    print word,'\t',n
