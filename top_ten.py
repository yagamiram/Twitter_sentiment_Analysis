import sys
import json

def main():
	
	tweet_file = open(sys.argv[1])
	hash_tag_dict = {}
	for each_tweet in tweet_file.readlines():
		each_tweet_dict = json.loads(each_tweet)
		if 'entities' in each_tweet_dict:
			hash_tags = each_tweet_dict['entities']['hashtags']
			for each_value in hash_tags:
				tag = each_value['text'].encode('utf-8')
				#print tag
				if tag in hash_tag_dict:
					hash_tag_dict[tag] += 1
				else:
					hash_tag_dict[tag] = 1
	#print hash_tag_dict.items()
	count = 0
	for tag, value in hash_tag_dict.items():
		if count < 10:
			print tag, value
			count += 1
if __name__ == '__main__':
    main()
