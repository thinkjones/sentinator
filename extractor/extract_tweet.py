import json
import tempfile
from collections import defaultdict
from subprocess import call

import requests
import twitter
from easysettings import EasySettings

settings = EasySettings('settings.txt')

# Auth Twitter
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
api = twitter.Api(consumer_key=settings.get('CONSUMER_KEY'),
                  consumer_secret=settings.get('CONSUMER_SECRET'),
                  access_token_key=settings.get('ACCESS_TOKEN'),
                  access_token_secret=settings.get('ACCESS_TOKEN_SECRET'))
api.VerifyCredentials()

# Get User Tweets
statuses = api.GetUserTimeline(screen_name='realdonaldtrump')

# Write them to file
fp = tempfile.NamedTemporaryFile()
fp.write(b' '.join([s.text for s in statuses]).encode("utf-8"))
fp.flush()
print(fp.name)

# Run Sentiment Analysis
call('cd nlp/stanford'.split(' '))
temp_output_dir = tempfile.gettempdir()
command_line = 'java -cp nlp/stanford/* -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse,sentiment -file {filename} -outputFormat json -outputDirectory {od}'.format(filename=fp.name, od=temp_output_dir)
args = command_line.split(' ')
call(args)
output_filename = '{fn}.json'.format(fn=fp.name)
fp.close()

# Read analysis as json
analysis_as_text = None
with open(output_filename, 'r') as fin:
    analysis_as_text = fin.read()
analysis_json = json.loads(analysis_as_text)

# Collate Sentiment Results
results = defaultdict(int)
for s in analysis_json.get('sentences'):
    results[s.get('sentiment')] += 1

# Pretty Print Results
for k, v in results.iteritems():
    print '{k}: {v}'.format(k=k, v=v)
