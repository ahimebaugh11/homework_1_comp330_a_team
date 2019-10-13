

class header_obj:
    def __init__(self, title):
        print("New Header "+title)
        self.title = title
        self.connected = []
        self.restricted = []
        self.possible = []
    
    def add_connected(self, item):
        self.connected.append(item)
    
    def add_restricted(self, item):
        self.restricted.append(item)

    def add_possible(self, item):
        self.possible.append(item)


class item_obj1:
    def __init__(self, title):
        print("New Item "+title)
        self.title = title
        self.connected = []
        self.restricted = []
        self.possible = []
    
    def add_connected(self, item):
        self.connected.append(item)
    
    def add_restricted(self, item):
        self.restricted.append(item)
    
    def add_possible(self, item):
        self.possible.append(item)

class item_obj2:
    def __init__(self, title):
        print("New Item "+title)
        self.title = title
        self.connected = []
        self.restricted = []
        self.possible = []
    
    def add_connected(self, item):
        self.connected.append(item)
    
    def add_restricted(self, item):
        self.restricted.append(item)
    
    def add_possible(self, item):
        self.possible.append(item)

class item_obj3:
    def __init__(self, title):
        print("New Item "+title)
        self.title = title
        self.connected = []
        self.restricted = []
        self.possible = []
    
    def add_connected(self, item):
        self.connected.append(item)
    
    def add_restricted(self, item):
        self.restricted.append(item)
    
    def add_possible(self, item):
        self.possible.append(item)


class puzzle_solver:

    def file_reader(self, file):
        print("Reading File")
        #opens and reads text file into a dictionary
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
    
    def puzzle_reader(self, puzzle):
        print("Reading Puzzle")
        header = []
        items1 = []
        items2 = []
        items3 = []
        clues  = []
        #fills puzzle into the above arrays
        for x in puzzle:
            for y in puzzle[x]:
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

   

    def clue_process(self, clue, headers, items1, items2, items3):
        
        clue = clue.split(',')
        
        all_objs  = headers+items1+items2+items3

        for x in all_objs:
            title = x.title

            # Finds correct object to add connections or restrictions
            if title == clue[0]:
                item_mod = x
                clue.remove(clue[0])

                # Goes through each piece of the clue
                for x in clue:
                    x = x.split(' ')

                    # Finds correct object to connect or restrict
                    for y in all_objs:
                        title = y.title
                        if title == x[2]:

                            temp_item = y

                            # Restricts
                            if(x[1] == 'NOT'):
                                       
                                

                                #restricts all items connected to the newly restricted item
                                for x in item_mod.connected:
                                    if x not in temp_item.restricted:
                                        temp_item.add_restricted(x)

                                #restricts the opposite direction
                                for x in temp_item.connected:
                                    if x not in item_mod.restricted:
                                        item_mod.add_restricted(x)
                                
                                item_mod.add_restricted(temp_item)
                                temp_item.add_restricted(item_mod)
                                break
                            # Connects
                            elif(x[1] == 'AND'):
                                

                                #connects all of the newly connected item's connections
                                for x in item_mod.connected:
                                    if x not in temp_item.connected:
                                        temp_item.add_connected(x)

                                #same the opposite direction
                                for x in temp_item.connected:
                                    if x not in item_mod.connected:
                                        item_mod.add_connected(x)

                                item_mod.add_connected(temp_item)
                                temp_item.add_connected(item_mod)
                                       
                                
                                break
                            # Marks object as a possible connection
                            elif(x[1] == 'MAYBE'):
                                 
                                item_mod.add_possible(temp_item)
                                break
                            
                break


    def item_creator(self, headers, items1, items2, items3):
        head_arr = []
        for x in headers:
            head_arr.append(header_obj(x))

        items1_arr = []
        for x in items1:
            items1_arr.append(item_obj1(x))

        items2_arr = []
        for x in items2:
            items2_arr.append(item_obj2(x))

        items3_arr = []
        for x in items3:
            items3_arr.append(item_obj3(x))



        return head_arr, items1_arr, items2_arr, items3_arr

                
    def puzzle_solve(self, headers, items1, items2, items3): 
        
        while(len(items1) > 0 and len(items2) > 0 and len(items3) > 0):     
            for x in headers:
                temp_items1 = items1
                temp_items2 = items2
                temp_items3 = items3  
                print("=========================================")
                print(x.title+": ")
                for y in x.restricted:
                    if(y.__class__.__name__ == "item_obj1" and y in temp_items1):
                        temp_items1.remove(y)
                    elif(y.__class__.__name__ == "item_obj2"and y in temp_items2):
                        temp_items2.remove(y)
                    elif(y.__class__.__name__ == "item_obj3"and y in temp_items3):
                        temp_items3.remove(y)
                if len(temp_items1) == 1:
                    items1.remove(temp_items1[0])
                    print("item 1: ")
                    print(temp_items1[0])
                elif len(temp_items2) == 1:
                    items2.remove(temp_items2[0])
                    print("item 2: ")
                    print(temp_items2[0])
                elif len(temp_items3) == 1:
                    items3.remove(temp_items3[0])
                    print("item 3: ")
                    print(temp_items3[0])

                
                
                
                
            

    



    def main(self):
        print("Running Main")
        puzzle = self.file_reader("puzzle.txt")
        
        headers, items1, items2, items3, clues = self.puzzle_reader(puzzle)

        headers, items1, items2, items3 = self.item_creator(headers, items1, items2, items3)
        
        for x in clues:
            self.clue_process(x, headers, items1, items2, items3)

        self.puzzle_solve(headers, items1, items2, items3)
        all_objs  = headers+items1+items2+items3
        '''for x in all_objs:
            print(x.title)
            print("Connected:")
            for y in x.connected:
                print(y.title)
            print("Restricted:")
            for y in x.restricted:
                print(y.title)
            print("Possible:")
            for y in x.possible:
                print(y.title)
            print("=================================================")'''



p = puzzle_solver()
p.main()










