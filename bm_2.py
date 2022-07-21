def tournament_maker(txt, n):
    f = open(txt, "r")
    new = f.read()
    s = new.split("\n")
    t=[[int(y) for y in x] for x in [list(x) for x in s]]
    ff = []
    for x in t:
        index_list = [0]
        final_list = []
        ffinal = []
        for i in range(n-1, n ^ 2-3*n+4, n-2):
            index_list.append(i)
        for i in range(n-1):
            final_list.append(x[index_list[i]:index_list[i+1]])
        for llst in final_list:
            lst = [0] * (n-len(llst))
            lst.extend(llst)
            ffinal.append(lst)
        if len(ffinal) != n:
            ffinal.append([0] * n)
        for i in range(len(ffinal)):
            for j in range(i+1, n-1):
                if ffinal[i][j] == 0:
                    ffinal[j][i] = 1
        ff.append(ffinal)
    return ff
