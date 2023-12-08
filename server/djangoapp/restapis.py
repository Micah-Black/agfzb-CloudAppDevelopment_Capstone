import requests
import json
# import related models here
from .models import CarDealer
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
                                     if api_key:
                                    # Basic authentication GET
                                     request.get(url, params=params, auth=, ...)
                                    else:
                                     # no authentication GET
                                     request.get(url, params=params)
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
def get_dealer_reviews_from_cf(url, dealerId=dealer_id):
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        # - Parse JSON results into a DealerView object list
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            reviews_doc = reviews["doc"]
            # Create a DealerReview object with values in `doc` object
            dealer_obj = DealerReview(dealership=dealership_doc["dealership"], name=name_doc["name"], purchase=purchase_doc["purchase"], review=review_doc["review"], purchase_date=purchase_date_doc["purchase_date"], car_make_doc["car_make"], car_model_doc["car_model"], car_year_doc ["car_year"], ...
review_obj.sentiment = analyze_review_sentiments(review_obj.review), id=id_doc["dealer_id"])
            results.append(reviews_obj)

    return results


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
def analyze_review_sentiments(dealerreview):
# def analyze_review_sentiments(text):
get_request(url, **kwargs)
  params = dict()
  params["text"] = kwargs["text"]
  params["version"] = kwargs["version"]
  params["features"] = kwargs["features"]
  params["return_analyzed_text"] = kwargs["return_analyzed_text"]
  response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



