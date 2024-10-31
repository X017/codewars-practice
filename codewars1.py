


def digital_root(n):
    nSum = 0
    for i in str(n):
        nSum += int(i)
    root = 0    
    for v in str(nSum):
        root += int(v)
    if len(str(root)) >= 2:
        rootResult = 0
        for net in str(root):
            rootResult += int(net)
        return rootResult
    else:
        return root


