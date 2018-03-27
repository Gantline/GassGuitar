from markov_python.cc_markov import MarkovChain
#standard parser
mc = MarkovChain()

#mc.add_file('C:/Users/Chris/PycharmProjects/CodeCademy/venv/text files/carols.txt')
#mc.add_file('C:/Users/Chris/PycharmProjects/CodeCademy/venv/text files/farie tales.txt')
#mc.add_file('C:/Users/Chris/PycharmProjects/CodeCademy/venv/text files/50Shades.txt')
#mc.add_file('C:/Users/Chris/PycharmProjects/CodeCademy/venv/text files/lovecraft.txt')
#mc.add_file('C:/Users/Chris/PycharmProjects/CodeCademy/venv/text files/songdata.txt')
mc.add_file('C:/Users/Chris/PycharmProjects/CodeCademy/venv/text files/bass_guitar_tabs.txt')
lyrics = mc.generate_text(20)

def printChain(L):
    s = "\n"
    while len(L) > 0:
        s = s + L.pop(0) + " "
    return s

print printChain(lyrics)