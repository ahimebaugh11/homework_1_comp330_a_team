

class header_obj:
    def __init__(self, title):
        self.title = title
        self.connected = []
        self.restricted = []
    
    def add_connected(item):
        connected.append(item)
        item.add_connected(title)
    
    def add_restricted(item):
        restricted.append(item)
        item.add_restricted(title)

class item_obj:
    def __init__(self, title):
        self.title = title
        self.connected = []
        self.restricted = []
    
    def add_connected(item):
        connected.append(item)
        item.add_connected(title)
    
    def add_restricted(item):
        restricted.append(item)
        item.add_restricted(title)

class puzzle_solver:

    def file_reader(file):
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
    
    def puzzle_reader(puzzle):
        header = []
        items1 = []
        items2 = []
        items3 = []
        clues  = []
        for x in puzzle:
            #print(x)
            for y in puzzle[x]:
                #print(y)
                if(x == 'HEADER\n'):
                    y = y[:-1]
                    header.append(y)
                elif(x == 'SECTION1\n'):
                    y = y[:-1]
                    items1.append(y)
                elif(x == 'SECTION2\n'):
                    y = y[:-1]
                    items2.append(y)
                elif(x == 'SECTION3\n'):
                    y = y[:-1]
                    items3.append(y)
                elif(x == 'CLUES\n'):
                    y = y[:-1]
                    clues.append(y)

        return header, items1, items2, items3, clues

   

    def clue_process(clue, headers, items1, items2, items3):
        clue = clue.split(',')
        item_mod = clue[0]
        clue.remove(item_mod)

        for x in clue:
            x = x.split(' ')
            if(x[0] == 'NOT'):
                
                
            

    




    puzzle = file_reader("puzzle.txt")
    headers, items1, items2, items3, clues = puzzle_reader(puzzle)


    #for x in headers:
        #x = header_obj(x)

    #for x in items1:
        #x = item_obj(x)

    #for x in items2:
        #x = item_obj(x)

    #for x in items3:
        #x = item_obj(x)

    for x in clues:
        clue_process(x, headers, items1, items2, items3)













