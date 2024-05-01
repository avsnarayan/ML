import urllib.request
import json
import os
import ssl


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context


# this line is needed if you use self-signed certificate in your scoring service.
allowSelfSignedHttps(True)

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
    "input_data": {
        "input_string": [
            {
                "role": "user",
                "content": "UnformattedDesc is informatted informatioon of a product. generate an enhanced and summarized description of the product.\
                Focus on extracting and summarizing factual attributes such as description, ingredients, color, size, dimensions, brand, and sub-brand names. \
                Avoid using superlatives or expressive language. Provide the most relevant top keyword for each product. \
                UnformattedDesc={UnformattedDesc}"
            }
        ],
        "parameters": {
            "temperature": 0,
            "max_tokens": 64,
            "top_p": 1,
            "do_sample": True
        }
    }
}
def suarize(UnformattedDesc):
    data['input_data']['input_string'][0]['content'] = data['input_data']['input_string'][0]['content'].format(UnformattedDesc=UnformattedDesc)
    body = str.encode(json.dumps(data))
    url = 'https://taxcat-llm.eastus2.inference.ml.azure.com/score'
    # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
    api_key = '1ay7QtHKPQlwJHzldVa1pfRSWmX2TFUf'
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type': 'application/json', 'Authorization': (
        'Bearer ' + api_key), 'azureml-model-deployment': 'mistralai-mixtral-8x7b-instru-5'}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = json.loads(response.read())
        return result['output']
    except urllib.error.HTTPError as error:
        #print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        #print(error.info())
        #print(error.read().decode("utf8", 'ignore'))
        return None
