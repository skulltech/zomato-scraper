import requests
import json


def main():
	restaurants = []

	category = 14
	categories = {
		1: 'Delivery',
		2: 'Dine-out',
		3: 'Nightlife',
		4: 'Catching-up',
		5: 'Takeaway',
		6: 'Cafes',
		7: 'Daily Menus',
		8: 'Breakfast',
		9: 'Lunch',
		10: 'Dinner',
		11: 'Pubs and Bars',
		13: 'Pocket Friendly Delivery',
		14: 'Clubs and Lounges'
	}
	
	payload = {
		'entity_id': 1,
		'entity_type': 'city',
		'category': category
	}

	headers = {'user-key': 'b79e96869e3f14a2e2a4e8b65595ce60'}	

	results = requests.get('https://developers.zomato.com/api/v2.1/search', params=payload, headers=headers).json()['results_found']
	iters = int(results / 20)

	with open('{}.json'.format(categories[category]), mode='w') as f:
		for i in range(iters):
			payload['start'] = (iters*20)
			payload['count'] = 20

			try:
				response = requests.get('https://developers.zomato.com/api/v2.1/search', params=payload, headers=headers).json()
				restaurants = restaurants + response['restaurants']
			except:
				json.dump(restaurants, f)
				raise
			else:
				continue
				
		json.dump(restaurants, f)


if __name__=='__main__':
	main()
