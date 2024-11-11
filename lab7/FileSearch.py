import os
# Implementing File search
def filesearch(dirpath, filenames, casesensitive=False):
    # Making BaseCase for recursion
    if not os.path.isdir(dirpath):
        return 0
    # Checking files in the dir list
    files = os.listdir(dirpath)
    cnt = 0;
    # Putting a loop to check each file in the dir
    for file in files:
        # Calling recursive call
        cnt += filesearch(os.path.join(dirpath, file), filenames, casesensitive)
        for file2 in filenames:
            if not casesensitive:
                file = file.lower()
                file2 = file2.lower()
            if file == file2:
                print(os.path.join(dirpath, file))
                cnt+=1
    return cnt
