# The Sentinator
A tool for measuring setiment, well more of a playground trying out different techniques.  This analyses @realDonaldTrumps recent 
tweets and marks them as positive, negative, or neutral.

# The Rough Plan
* Pick a subject - Twitter handle - realdonaldtrump - DONE
* Move through time and measure sentiment of tweet. - DONE For Recent Tweets
* Calculate sentiment Value based off historical values with older values decaying in their influence on present value. - NOT DONE
* Record daily changes in sentiment. - NOT DONE


# Setup

## Python
```
sudo virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Java
Download this file `http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip` in this directory `nlp/standford`.


# NLP Examples
Example:
```
java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt
```

Sentiment Example:
```
java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse,sentiment -file input.txt -outputFormat json
```

# Run
```
python extractor/extract_tweet.py
```

Example Output:
```
Annotation pipeline timing information:
TokenizerAnnotator: 0.1 sec.
WordsToSentencesAnnotator: 0.0 sec.
POSTaggerAnnotator: 0.1 sec.
ParserAnnotator: 3.5 sec.
SentimentAnnotator: 0.2 sec.
TOTAL: 3.9 sec. for 446 tokens at 115.6 tokens/sec.
Pipeline setup: 1.6 sec.
Total time for StanfordCoreNLP pipeline: 5.7 sec.
Positive: 5
Neutral: 8
Negative: 19
```

