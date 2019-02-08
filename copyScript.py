import os

# Replace this string with your netIDs -- keep the ', ' format!
files = "rkg2, rlc14, rup1, ryw3, sc83, sdm9, sfn1, sg62, sg71, sj49, sk103, smg10, stx1"

# YOU HAVE TO CHANGE THE PATH YOURSELF
def copyContents(stringNetIDs):
    '''
    Given a string of netIDs, inserts its corresponding log file into the scoring-template file.
    Then, it takes the final result and writes it to a new txt file whose name is a netID.
    Input: 
        stringNetIDs -- a single string of all the netIDs. The string is formatted like this
                        such that .split() works:
                            "ac99, kk49, jw68, sc80"
    Output:
        None
    '''
    cur_path = os.path.dirname(__file__)

    # Split the netIDs on ', '
    netIDs = stringNetIDs.split(', ')
    # For each of the given netIDs
    for netID in netIDs:
        # Open the template file and store its contents
        with open("scoring-template.txt", 'r') as s:
            template = s.readlines()

        templateLength = len(template)
        templateCopy = template

        # Create the relative path to the log files (autograder files)
        # CHANGE THE RELATIVE PATH
        autograderPath = os.path.relpath('autograder\\' + netID + '.log', cur_path)
        # Create the relative path to the final txt files (Where you want your grade files)
        # CHANGE THE RELATIVE PATH
        gradesPath = os.path.relpath('grades\\' + netID + '.txt', cur_path)
        # Open the log file and copy its contents
        with open(autograderPath, 'r') as f:
            data = f.readlines()

        # Initialize the starting index -- right after 
        # the '<Insert the autograder code here>' line
        idx = templateLength - 4
        # Essentially erase the <Insert ... > line
        templateCopy[templateLength - 1] = '\n'
        # For each of log file lines
        for line in data:
            # If we are still in bounds of the opened template,
            # then replace the index with the line found in the log file.
            if idx < templateLength:
                templateCopy[idx] = line
                idx += 1
            else:
                # Else, just append the line to the end of the array.
                templateCopy.append(line)
        # Add the overwritten lines back to the array
        templateCopy.append("\n")
        templateCopy.append("------------------------------------------------------------------------------\n")
        templateCopy.append("\n")
        templateCopy.append("TOTAL                                                                   ?/100\n")

        # Create/Open the final .txt file, and write the final contents to it.
        with open(gradesPath, 'w') as w:
            for line in templateCopy:
                w.write(line)
    return

copyContents(files)