import requests


def scrape():
	restaurants = []

	category = 2
	payload = {
		'entity_id': 1,
		'entity_type': 'city',
		'category': category,
		'start': start,
		'count': count
	}

	headers = {'user-key': 'b79e96869e3f14a2e2a4e8b65595ce60'}	

	results = requests.get('https://developers.zomato.com/api/v2.1/search', params=payload, headers=headers).json()['results_found']
	iters = int(results / 20) + 1

	for i in range(iters):
		payload['category'] = category
		payload['start'] = (iters*20)
		payload['count'] = 20

		response = requests.get('https://developers.zomato.com/api/v2.1/search', params=payload, headers=headers).json()
		restaurants = restaurants + response['restaurants']
