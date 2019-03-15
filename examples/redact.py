import sys
import fitz
from fitz.utils import getColor

def mark_word(page, text):
    """Underline each word that contains 'text'.
    """
    found = 0
    col=(0,0,0)                        # black color

    wlist = page.getTextWords()        # make the word list
    for w in wlist:                    # scan through all words on page
        if text in w[4]:               # w[4] is the word's string
            found += 1                 # count
            r = fitz.Rect(w[:4])       # make rect from word bbox
            #page.addRectAnnot(r)       # Rectangle         
            page.drawRect(r,col,fill = col, width = 1, dashes = None, roundCap = True, overlay= True, morph = None)
            page.insertText(r[0:2], 'xxx', fontsize = 11) #Replace word so it cant be searched for  - not working as I thought!
                        
    return found

fname = sys.argv[1]                    # filename
#text = sys.argv[2]                     # search string
text=['mike','rerer','Lorem','Hampden-Sydney','College','loves']
doc = fitz.open(fname)

doc.setMetadata({})                    # clear metadata
doc._delXmlMetadata()                  # clear any XML metadata

new_doc = False                        # indicator if anything found at all

for page in doc:                       # scan through the pages

    for word in text:
        print("Redacting word '%s' in document '%s'" % (word, doc.name))
        found = mark_word(page, word)      # mark the page's words
        if found:                          # if anything found ...
            new_doc = True
            print("found '%s' %i times on page %i" % (word, found, page.number + 1))

if new_doc:
    doc.save("marked-" + str(doc.name).split('/')[-1])


# WORKING VERSION FOR A SINGLE WORD
# fname = sys.argv[1]                    # filename
# text = sys.argv[2]                     # search string
# doc = fitz.open(fname)

# print("underlining words containing '%s' in document '%s'" % (text, doc.name))

# new_doc = False                        # indicator if anything found at all

# for page in doc:                       # scan through the pages
#     found = mark_word(page, text)      # mark the page's words
#     if found:                          # if anything found ...
#         new_doc = True
#         print("found '%s' %i times on page %i" % (text, found, page.number + 1))

# if new_doc:
#     doc.save("marked-" + str(doc.name).split('/')[-1])
