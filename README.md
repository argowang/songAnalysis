# songAnalysis
NLP Analysis on Chinese Songs with THULAC Toolkit

This project aims to use data analysis and nlp tools to find out the "culture" and pattern behind chinese hip-hop music.
Words appeared the most could be considered as the heart of the hip-hop culture and the value of East-Asia culture

Another interesting analysis to be done is finding out which rhyme pairs are most popular among hip-hop music.
Rhyme is considered as a value linguistics property in Chinese. The discovery of the frequency of rhyme pairs in 
hip-hop music(whose lyric is common and similar to conversation) may shed light onto Chinese Linguistics problem.

The other analysis to be done is to classify a hip-hop song as positive or negative based on the pre-annotated 
adj and noun appeared in the lyrics. 

THULAC is an NLP toolkit that is easy to use while maintain a high level of accuracy in parsing.
You can find the toolkit over here: http://thulac.thunlp.org/
However, the toolkit has limited its function to parsing (or you can say it concentrates all its energy on parsing).
As a result, the toolkit needs some setup before usage.
However, it is obvious that many of the setups are redundent and there might be some traps if you are not 
familiar with the toolkit or you are a beginner. For example: If you are using Python2, it is very likely that 
the chinese character printed out is unreadable code. I encountered the same problem during my work.
Therefore I wish my code may provide some extents of help.

Module needed:

THULAC

Pyecharts (for visualization)

requests

bs4

=======================Aug 30th update

Implement the scraping module

By entering the singers' id on the music.163.com, the web scraping module will gather all of singers' songs and lyrics. 
This largely increase the efficiency of collecting data and improve the analysis outcome.

=======================Aug 31st update

Add in function to remove unwanted word. The original parsing results involve many unwanted English word and meaningless
word. The function helps to clean up the result.

Modify visualization part so that the visualization html file is generated in the same directory as the code.



TODO:

Extract every chinese character at end of each line. Put into a single array

Transcribe this array to Pinyin

Use previous project to transcribe Pinyin into rhyme

Analyze the most frequently showing rhyme pairs

Classify song based on adj. and n.

