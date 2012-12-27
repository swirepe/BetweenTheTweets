#!/usr/bin/python

""" This script goes through a literotica mirror and parses
the sentences out of the stories.

   special thanks to Batitia, who helped me regain a handle on nltk
   on Christmas day.  (she's a PhD student in Computational Lingustics,
   and a really good sport: @snatiabir )

"""


from BeautifulSoup import BeautifulSoup
import glob
import os
import sys
## make sure you run nltk.download() and get the punkt package
import nltk



## run `getlit.sh` first if you want to play along
files = glob.glob("./literotica.com/storyxs/stories/*.shtml")

def getTexts(files):
    for f in files:
        rawtext = open(f).read()
        soup = BeautifulSoup(rawtext, convertEntities=BeautifulSoup.HTML_ENTITIES)


        ## this seems to be the body of text, 
        ## but other non-story elements have the same structure
        #td align="left" width="535" 
        biguns = soup.findAll("td", width="535")
        
        maxtex = ''
        maxlen = -1
        
        for bigun in biguns:
            bigunlen = len(bigun.getText())
            if bigunlen > maxlen:
                maxlen = bigunlen
                maxtext = bigun.getText().replace("  ", '')
                                                                    
                
                
        yield  "\n%\n".join([x.replace("\r\n", '') for x in nltk.sent_tokenize(maxtext)])

        

stories = getTexts(files)
i = 0
for story in stories:
    outname = os.path.join("collected", "%05d.txt" % i)
    out = open(outname, 'w')
    out.write(story.encode('utf-8'))
    out.close()
    i += 1
    
    
