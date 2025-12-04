# project-10a

# Gabriel Venegas
# GitHub username: GVenegas1
# Date: 12/03/2025

def file_sum(filename):
    """This function reads numbers from the file name given by 'filename'.
    It adds them together and writes the total to a file named sum.txt"""

    #Start running total
    total = 0

    #Open the file to read the numbers line by line
    with open(filename, "r") as infile:
        for line in infile:

            #Removes extra characters
            clean_line = line.strip()

            #Convert the text into a float
            number = float(clean_line)

            #Add to the running total
            total += number

    #write the final total into the new txt file
    with open("sum.txt", "w") as outfile:
        outfile.write(str(total))


#if __name__ == "__main__":
#   file_sum("numbers.txt")
#   print("done!check sum of result")