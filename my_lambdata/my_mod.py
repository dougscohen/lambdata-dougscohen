# my_lambdata/my_mod.py

def convert_to_seconds(cell):
    ''' 
    This function is used to convert a string time in the form of
    minutes:seconds to total number of seconds
    '''
    Y = (int(cell.split(':')[0]) * 60) + (int(cell.split(':')[1]))
    return Y

def state_abbrev(state):
    if state == 'Alabama':
        return 'AL'
    elif state == 'Alaska':
        return 'AK'
    elif state == 'Arizona':
        return 'AZ'
    elif state == 'Arkansas':
        return 'AR'
    elif state == 'California':
        return 'CA'
    elif state == 'Colorado':
        return 'CO'
    elif state == 'Connecticut':
        return 'CT'
    elif state == 'Delaware':
        return 'DE'
    elif state == 'Florida':
        return 'FL'
    elif state == 'Georgia':
        return 'GA'
    elif state == 'Hawaii':
        return 'HI'
    elif state == 'Idaho':
        return 'ID'
    elif state == 'Illinois':
        return 'IL'
    elif state == 'Indiana':
        return 'IN'
    elif state == 'Iowa':
        return 'IA'
    elif state == 'Kansas':
        return 'KS'
    elif state == 'Kentucky':
        return 'KY'
    elif state == 'Louisiana':
        return 'LA'
    elif state == 'Maine':
        return 'ME'
    elif state == 'Maryland':
        return 'MD'
    elif state == 'Massachusetts':
        return 'MA'
    elif state == 'Michigan':
        return 'MI'
    elif state == 'Minnesota':
        return 'MN'
    elif state == 'Mississippi':
        return 'MS'
    elif state == 'Missouri':
        return 'MO'
    elif state == 'Montana':
        return 'MT'
    elif state == 'Nebraska':
        return 'NE'
    elif state == 'Nevada':
        return 'NV'
    elif state == 'New Hampshire':
        return 'NH'
    elif state == 'New Jersey':
        return 'NJ'
    elif state == 'New Mexico':
        return 'NM'
    elif state == 'New York':
        return 'NY'
    elif state == 'North Carolina':
        return 'NC'
    elif state == 'North Dakota':
        return 'ND'
    elif state == 'Ohio':
        return 'OH'
    elif state == 'Oklahoma':
        return 'OK'
    elif state == 'Oregon':
        return 'OR'
    elif state == 'Pennsylvania':
        return 'PA'
    elif state == 'Rhode Island':
        return 'RI'
    elif state == 'South Carolina':
        return 'SC'
    elif state == 'South Dakota':
        return 'SD'
    elif state == 'Tennessee':
        return 'TN'
    elif state == 'Texas':
        return 'TX'
    elif state == 'Utah':
        return 'UT'
    elif state == 'Vermont':
        return 'VT'
    elif state == 'Virginia':
        return 'VA'
    elif state == 'Washington':
        return 'WA'
    elif state == 'West Virginia':
        return 'WV'
    elif state == 'Wisconsin':
        return 'WI'
    elif state == 'Wyoming':
        return 'WY'
    elif state == 'District of Columbia':
        return 'DC'
    else:
        return 'Territory'


if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    test = '1:14'
    print(convert_to_seconds(test))
    print(state_abbrev('North Carolina'))
    print(state_abbrev('District of Columbia'))
    print(state_abbrev('Puerto Rico'))


    

