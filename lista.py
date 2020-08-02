qpa = ['copa', 'ananas','wawa', 'opa','wawrka','pola']
spam = ['jabłka', 'banany', 'tofu', 'koty']

def kod(spam):
    for i in range(len(spam)):
        if i == -1:
            print('i '+ spam[i], end='')

        elif i == 4:
            print(spam[i] + ', ', end='')

kod(spam)