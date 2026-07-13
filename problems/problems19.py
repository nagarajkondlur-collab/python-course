# problem : 19 merging 3 lists
def merge_alternate(list1, list2, list3):
    merged = []
    i = 0
    j = 0
    k = 0
    while i < len(list1) and j < len(list2) and k < len(list3):
        merged.append(list1[i])
        merged.append(list2[j])
        merged.append(list3[k])
        i = i+1
        j = j+1
        k = k+1
    return merged
print(merge_alternate([1,2],[10,20],[100,200]))

## slightly diffrent problem i use variables list here
def merge_alternate_strings(list1,list2):
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        merged.append(list1[i])
        merged.append(list2[j])
        i = i+1
        j = j+1
    return merged
print(merge_alternate_strings(["ABC"],["XYZ"]))
