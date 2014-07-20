import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#hw()
	#lines(sent_file)
	#lines(tweet_file)

	afinnfile = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items()
	tweetfile = open(sys.argv[2])
	for each_line in tweetfile.readlines():
		dict_list = json.loads(each_line)
		if 'text' in dict_list:
			print scores.get(dict_list['text'].encode('utf-8'),0)
				
				
	 
		
if __name__ == '__main__':
    main()
