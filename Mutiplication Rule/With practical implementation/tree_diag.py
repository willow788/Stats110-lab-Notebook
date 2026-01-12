#tree diagram representation
def printing_tree(A, B):
    for a in A:
        print(a)
        for b in B:
            print("|_", b)
printing_tree(A, B)
