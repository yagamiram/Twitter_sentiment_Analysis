import sys
import json
POSITIVE = 1
NEGATIVE = -1
NEUTRAL	= 0
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	afinnfile = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	new_word_dict = {}
	for each_tweet in tweet_file.readlines():
		tweet_sentiment = NEUTRAL
		total_value = 0
		new_word_list = []
		each_tweet_dict = json.loads(each_tweet)
		if 'text' in each_tweet_dict:
			tweet_text = each_tweet_dict['text'].encode('utf-8')
			sentiment_value = scores.get(tweet_text,0)
			if sentiment_value > 0:
				tweet_sentiment = POSITIVE
			elif sentiment_value < 0:
				tweet_sentiment = NEGATIVE
			for each_word in tweet_text.split():
				#print each_word
				if each_word in scores:
					total_value += scores[each_word]
				else:
					new_word_list.append(each_word)
			for each_word in new_word_list:
				if each_word not in new_word_dict:
					new_word_dict[each_word] = [total_value, 1]
				else:
					sentiment = new_word_dict[each_word]
					sentiment[0] += total_value
					sentiment[1] += 1
					new_word_dict[each_word] = sentiment					

	for each_key in new_word_dict:
		sentiment = new_word_dict[each_key]
		#print sentiment
		print each_key, (sentiment[0]/sentiment[1])*5
if __name__ == '__main__':
    main()
