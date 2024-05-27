import json,random,urllib.parse, datetime

mockSignature = "Joe Bloggs Mock Examinations Practise"
iboName = "Joe Bloggs Baccalaureate Organization"
currentDate = datetime.datetime.now().strftime("%B %d, %Y")
currentYear = str(datetime.datetime.now().year)
filename = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+"mockpaper2.html"

P2questions=json.loads(open("P2Q.json","r",encoding="UTF-8").read())
print(P2questions)
allQuestions=P2questions[0]+P2questions[1]+P2questions[2]+P2questions[3]
allJumble=False
fourQs=[]
if not allJumble:
    fourQs=[random.choice(questionSection) for questionSection in P2questions]
else:
    fourQs = random.sample(allQuestions, 4)
print(fourQs)
totalHTMLcode=""
for i in range(4): 
    myID=i+1
    filteredFourQsI = fourQs[i].replace("two","<b>two</b>")
    totalHTMLcode += f"<div>&nbsp; <b>{myID}. &nbsp;</b> {filteredFourQsI}</div><br />"
totalHTMLcode=urllib.parse.quote(totalHTMLcode)
copyrightcode=f"""&copy; {iboName}, {currentYear}

This mock paper is confidential information. 
Without permission from {iboName}, you may not 
distribute, copy, or modify it in any form. 

This is Joe Bloggs' internal revision material and not
to be shared publilcly."""
copyrightcode=copyrightcode.replace(" ","&nbsp;").replace("\n","<br />")
copyrightcode=urllib.parse.quote(copyrightcode)

myHTML = open("templatePaper2File.html","r",encoding="UTF-8").read()
myFinalHTML = myHTML.replace("[YOURCOPYRIGHTWARNINGHERE]",copyrightcode).replace("[INSERTMOCKPAPERSIGNATUREHERE]",mockSignature).replace("[INSERTCURRENTDATEHERE]",currentDate).replace("[INSERTIBONAMEHERE]",iboName).replace("[INSERTCURRENTYEARHERE]", currentYear).replace("[INSERTQUESTIONDATAHERE]",totalHTMLcode)
with open(filename, "w", encoding="UTF-8") as f:
    f.write(myFinalHTML)