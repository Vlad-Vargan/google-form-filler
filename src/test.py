
"""
Getting data from txt file 
in case questions startinf from nubmers 
and each have 5  answers
"""

def get_data():
    f = open('/home/vargan/Dropbox/Programming_projects/Google Forms/test1.txt')
    questions = [q for q in f if q[0].isdigit()]
    f.close()

    f = open('/home/vargan/Dropbox/Programming_projects/Google Forms/test1.txt')
    answers = []
    l = []
    j = 0
    for a in f:
        if j == 6:
            j = 0
            answers.append(l[:])
            l.clear()
        if j > 0:
            l.append(a)
        j +=1
    f.close()
    return questions, answers

"""
    <input 
    type="text" 
    class="quantumWizTextinputSimpleinputInput exportInput" 
    jsname="YPqjbf" 
    autocomplete="on" 
    tabindex="0" 
    aria-label="option value" 
    value="Option 1" 
    dir="ltr" 
    data-initial-value="Option 1"
    >

"""