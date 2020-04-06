# my_lambdata/my_mod.py

def convert_to_seconds(cell):
    ''' 
    This function is used to convert a string time in the form of
    minutes:seconds to total number of seconds
    '''
    Y = (int(cell.split(':')[0]) * 60) + (int(cell.split(':')[1]))
    return Y

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    test = '1:14'
    print(convert_to_seconds(test))