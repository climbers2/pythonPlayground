def getFileLineCount(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
    return i+1
print("line count is ",getFileLineCount("testText.txt"))


    
