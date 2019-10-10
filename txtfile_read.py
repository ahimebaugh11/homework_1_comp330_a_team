def readPuzzle(file):
    with open(file) as my_file:
       puzzle = {}
       for line in my_file:
           if line.isupper():
               title = line
               puzzle[title] = []
           if line != '\n' and line != title:
               puzzle[title].append(line)
           else:
               continue 
    return(puzzle)
