import shutil

def get_width():
    size1 = shutil.get_terminal_size((80, 20))
    size2 = str(size1).replace("os.terminal_size(columns=","")
    size3 = size2[:-9]
    size4 = size3.replace(" ","")
    size5 = size4.replace(",","")
    actual_width = int(size5)
    return actual_width
