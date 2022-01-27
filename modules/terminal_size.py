import shutil

def getTermSize():
    aw = shutil.get_terminal_size((80, 20))
    ms = [
        aw[0],
        aw[1]
    ]
    return ms

