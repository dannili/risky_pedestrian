import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={
	"day_of_week": 3,
	"day_of_year": 145,
	"month": 5,
	"hour": 22,
	"neighbourhood_id": 62,
	"is_major_arterial": 1,
	"is_dry": 1,
	"good_light": 0,
	"good_visibility": 1,
	"has_traffctl": 1,
	"is_intersection": 0,
	"has_rlc": 0
	})

print(r.json())