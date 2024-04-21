import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


text="""Shah Rukh Khan, also known by the initialism SRK. He is an Indian actor and film producer who works in Hindi films as a King Khan. Referred to in the media as the "Baadshah of Bollywood" and "King Khan", he has appeared in more than 100 films. He earned numerous accolades, including 14 Filmfare Awards."""

def summarizer(rawdocs):
    stopwords=list(STOP_WORDS)
    # print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc=nlp(rawdocs)
    tokens=[token.text for token in doc]
    # print(tokens)
    word_freq={}

    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if  word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text] +=1
    # print(word_freq)
    max_freq=max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq

    # print(word_freq)
    sent_tokens=[sent for sent in doc.sents]
    # print(sent_tokens)
    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    # print(sent_scores)

    select_len=int(len(sent_tokens)*0.3)
    print(select_len)


    # from heapq import nlargest
    summary= nlargest(select_len,sent_scores,key=sent_scores.get)
    # print(summary)
    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)
    # print("\n\n","-"*20,"Original Text","-"*20)
    # print("\n",text,"\n")
    # print("Total Length :- ",len(text.split(' ')))
    # print("\n\n","-"*20,"Summarized Text","-"*20)
    # print("\n",summary,"\n")
    # print("Total Length :- ",len(summary.split(' ')),"\n\n")
    org_len=len(rawdocs.split(' '))
    summ_len=len(summary.split(' '))

    return summary,doc,org_len,summ_len