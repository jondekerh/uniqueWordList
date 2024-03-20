class getList:
    def __init__(self, file_path, alphanumeric = False, count = False):
        self.file_path = file_path
        self.alphanumeric = alphanumeric
        self.wordCount = []
        self.wordList = []

        with open(self.file_path, 'r') as infile:
            # if not counting iterations make a set
            if count == True:
                infile_sorted = sorted(infile.read().split())
                if alphanumeric == True:
                    cleaned_strings = ["".join(char for char in s if char.isalnum()) for s in infile_sorted]
                else:
                    cleaned_strings = ["".join(char for char in s if char.isalpha()) for s in infile_sorted]
                infile_cleaned = [i.lower() for i in cleaned_strings]
                for i in infile_cleaned:
                    if i != '':
                        match = False
                        for row in self.wordList:
                            if (row[0]) == i:
                                row[1] += 1
                                match = True
                                break
                        if not match:
                            self.wordList.append([i, 1])

            else:
                infile_sorted = sorted(set(infile.read().split()))
                # cleaning the strings of grammar and numbers if alphanumeric is off
                if alphanumeric == True:
                    cleaned_strings = ["".join(char for char in s if char.isalnum()) for s in infile_sorted]
                else:
                    cleaned_strings = ["".join(char for char in s if char.isalpha()) for s in infile_sorted]
                # all lowercase
                infile_cleaned = [i.lower() for i in cleaned_strings]
                # making the final list
                for i in infile_cleaned:
                    if i != '':
                        if i not in self.wordList:
                            self.wordList.append(i)

            self.wordCount = len(self.wordList)
