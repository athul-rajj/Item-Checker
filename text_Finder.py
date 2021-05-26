# Text finder

class Finder:

    def __init__():
        pass

    def noEnd(text, keyword):
        length = len(keyword)

        index = 0
        indexLast = length - 1

        keyStart = index
        keyEnd = indexLast

        tie = False

        while True:
            
            if keyword in text:
                pass
            else:
                return None 
                break

            if text[index] == keyword[keyStart]:
                if text[indexLast] == keyword[keyEnd]:

                    output = text[indexLast + 1 : len(text) + 1]

                    return(output)
                    break

            index += 1
            indexLast += 1

    def searcher(text, keyword, end):

        length = len(keyword)

        index = 0
        indexLast = length - 1

        keyStart = index
        keyEnd = indexLast

        tie = False

        while True:
            if keyword in text:
                pass
            else:
                print('The keyword is not in the text...')
                break

            if text[index] == keyword[keyStart]:
                if text[indexLast] == keyword[keyEnd]:

                    output = text[index : len(text) + 1]

                    index = 0
                    indexLast = len(end) - 1

                    if keyword == end:
                        return(output)
                        tie = True

                    if tie == False:

                        while True:
                        
                            if end in output:
                                pass
                            else:
                                print('The ending term is not in the text...')
                                break

                            if output[index] == end[0]:
                                if output[indexLast] == end[len(end) - 1]:
                                    return(output[0 : indexLast + 1])
                                    break
                            index += 1
                            indexLast += 1
                            
                    break

            index += 1
            indexLast += 1

            
# README - Make a variable called text to put the text to read, then call Finder.searcher() and put text as the first instance, then put whatever you want to find
# Then put whatever you want to end it with

#Finder.noEnd takes a starting keyword and prints the remaining text

if __name__ == '__main__':

    text = 'Hello world, how are you today?'
    
    example_one = Finder.searcher(text, 'how', 'you')

    example_two = Finder.noEnd(text, 'world')

    print(example_one)
    print(example_two)
