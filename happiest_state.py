states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

import sys
import json
POSITIVE = 1
NEGATIVE = -1
NEUTRAL	= 0
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	tweetfile = open(sys.argv[2])
	new_state_dict = {}
	for each_line in tweetfile.readlines():
		dict_list = json.loads(each_line)
		if 'text' in dict_list:
			if 'place' in dict_list:
				if dict_list.get('place', None) != None:
					if dict_list['place']['name'] not in new_state_dict:
						#print dict_list['place']['name']
						state = dict_list['place']['name']
						#print state
						if state != None and state in states.values():
							state = states.keys()[states.values().index(state)]
							new_state_dict[state] = 1
					else:
						new_state_dict[state] += 1 
			elif 'user' in dict_list:
				#print dict_list['user']['location']
				if dict_list.get('user', None) != None:
					if dict_list['user']['location'] not in new_state_dict:
						#print dict_list['user']['location']
						state = dict_list['user']['location']
						#print state
						if state != None and state in states.values():
							state = states.keys()[states.values().index(state)]
							new_state_dict[state] = 1
					else:
						new_state_dict[state] += 1 
			
	happy_state = None
	max_value = 0
	#print new_state_dict.items()
	for each_key in new_state_dict:
		temp_value = new_state_dict[each_key] 
		if max_value < temp_value:
			max_value = temp_value
			happy_state = each_key

	print happy_state
if __name__ == '__main__':
    main()
