from BeautifulSoup import BeautifulSoup
import glob
import sys
import nltk

#td align="left" width="535"

files = glob.glob("./literotica.com/storyxs/stories/*.shtml")

def getTexts(files):
    for f in files:
        rawtext = open(f).read()
        soup = BeautifulSoup(rawtext, convertEntities=BeautifulSoup.HTML_ENTITIES)
        
        biguns = soup.findAll("td", width="535")
        
        maxtex = ''
        maxlen = -1
        
        for bigun in biguns:
            bigunlen = len(bigun.getText())
            if bigunlen > maxlen:
                maxlen = bigunlen
                maxtext = bigun.getText().replace("  ", '')
                
                
        yield "\n%\n".join([x.replace("\r\n", '') for x in nltk.sent_tokenize(maxtext)])
        sys.exit(0)
        
        

getTexts(files)
