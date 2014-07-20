import sys
import json
POSITIVE = 1
NEGATIVE = -1
NEUTRAL	= 0
def main():
	
	tweet_file = open(sys.argv[1])
	
	new_word_dict = {}
	total_count = 0
	for each_tweet in tweet_file.readlines():
		tweet_sentiment = NEUTRAL
		total_count = 0
		new_word_list = []
		each_tweet_dict = json.loads(each_tweet)
		if 'text' in each_tweet_dict:
			tweet_text = each_tweet_dict['text'].encode('utf-8')
			for each_word in tweet_text.split():
				total_count += 1
				if each_word in new_word_dict:
					new_word_dict[each_word] += 1
				else:
					new_word_dict[each_word] = 1
	for each_key in new_word_dict:
		print each_key, new_word_dict[each_key]/total_count
if __name__ == '__main__':
    main()
