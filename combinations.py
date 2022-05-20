class word_combs():

    def __init__(self, n : int, k : int=3, visualization : bool=False, block:bool=False, word : str = "aahed"):
        self.n = n
        self.k = k
        self.visualization = visualization
        self.block = block
        self.word = word
        self.dict = {}
        self.colors = ["Grey", "Yellow", "Green"] if self.visualization == False else ["\033[0;37m{}\033[0;0m","\033[0;33m{}\033[0;0m","\033[0;32m{}\033[0;0m"]
        self.sequences, self.instances  = [[] for i in range(self.n)], [[] for i in range(self.n)]
        self.combinations = []

        
        self.rotate()
        self.visualize()
        self.return_combination()
        self.delete()

    def return_combination(self):
        global combinations 
        combinations = self.combinations
       
    def rotate(self):
        for integer in range(self.n):
            for i in range(self.k**(self.n-(integer+1))): #k**(n-(z+1))) - decreases the exponent (n), +1 so the first step is already decreasing the exponent
                for x in range(self.k): #k - all options
                    self.sequences[integer].append(self.colors[x].format(self.word[integer])) if self.block == False else self.sequences[integer].append(self.colors[x].format('■'))
        for s in range(len(self.sequences)): #even out the lists
            quotient = int(self.k**self.n/len(self.sequences[s]))
            for element in self.sequences[s]:
                for each in range(quotient):
                    self.instances[s].append(element)
        for i in range(self.k ** self.n):
            for f in range(self.n):
                self.dict[str(f)] = self.instances[f][i]
            self.combinations.append(self.dict.copy())
    def delete(self):
        del self.sequences, self.instances
        
    def visualize(self):
        
        if self.visualization != True:
            print(f"All {len(self.combinations)} combinations for '{self.word[0:self.n]}' are calculated.")
        else:
            for i in range(len(self.combinations)):
                zeros = ""
                for x in range(len(str(self.k ** self.n)) - len(str(i+1))):
                    zeros += str(0)
                comb = f"{zeros}{i+1}: "
                for x in range(self.n):
                    comb += self.combinations[i][str(x)]

                print(comb)
    
    



class best():
    def __init__(self, n:int, k:int=3, detailed:bool=False, url:str="/Users/basti/Desktop/python/wordle/allowed_text.txt"):
        self.n = n
        self.k = k
        self.detailed = detailed
        self.url = url


        self.allowed_words = []
        self.allowed_words_pattern = []
        self.allowed_words_pattern_copy = self.allowed_words_pattern.copy()
        self.matrix = [[] for i in range(self.k ** self.n)]
        self.patterns = []
        self.confirmed_out = [[] for i in range(self.k ** self.n)]
        self.index = []

        self.word = "" 
        self.pattern = ""


        self.get_words()
        self.get_data()
        self.compare(k**n)
        #self.compare(10)


    def get_words(self):
        with open(self.url) as file:
            self.allowed_words = file.readlines()
    
    def get_data(self, iterations:int = 1):
        for i in range(len(self.allowed_words[0:iterations])):
            self.word = self.allowed_words[i]
            word_combs(self.n, self.k,word=self.word)
            for e in range(len(combinations)):
                for i in range(self.n):
                    self.matrix[e].append([i,combinations[e][str(i)]])
            self.create_pattern(name=self.word)
            
    def create_pattern(self, name):
        for matrixes in self.matrix:
            self.pattern = ""
            for duo in matrixes:
                if duo[1] == "Grey":
                    x = 0
                elif duo[1] == "Yellow":
                    x = 1
                elif duo[1] == "Green":
                    x = 2
                self.pattern += self.word[duo[0]] + str(x)
            self.patterns.append(self.pattern)
        
        for word in self.allowed_words:
            self.pattern = ""
            word = word[:self.n]
            for letter in word:
                self.pattern += letter + str(2)
            self.allowed_words_pattern.append(self.pattern)
        
        self.compare(name=name)

                
    def compare(self, name, iterations:int = 243 ):
        self.confirmed_out = [[] for i in range(self.k ** self.n)]
        self.allowed_words_pattern_copy = self.allowed_words_pattern.copy()      
        for i in range(len(self.patterns[0:iterations])):
            #print(f"{i+1}/{len(self.patterns[0:iterations])}", end="\r")
            
            for word in self.allowed_words_pattern_copy:
                for x in range(0,int(len(word)/2),2):
                    if self.patterns[i][x+1] == "0" and self.patterns[i][x] in word[x]:
                        self.confirmed_out[i].append(word) 
                        break
                    elif self.patterns[i][x+1] == "1" and self.patterns[i][x] == word[x]: 
                        self.confirmed_out[i].append(word)
                        break
                    elif self.patterns[i][x+1] == "2" and self.patterns[i][x] != word[x]:
                        self.confirmed_out[i].append(word) 
                        break



        print()
        x = 0
        for i in range(len(self.confirmed_out)):

            ø = len(self.confirmed_out[i]) / (self.k ** self.n )
        r = ø/len(self.allowed_words) 
        print(f"ø: {ø} \np: {r} \n\n") 
        self.delete()

        


    
        
        


word_combs(5,3,True,True)
#best(5,3)


