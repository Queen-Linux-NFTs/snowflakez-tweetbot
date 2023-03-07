from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import os
import json
import random
import time

load_dotenv()

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")

greetings = [
    'Plenty of SnowflakeZ for the picking!\n',
    'Find a unique Snowflake for a unique person\n',
    'Real Snowflakes aren\'t unique, but these SnowflakeZ are!\n',
    'Be ready for the next minting!\n',
    'It doesn\'t need to be the holidays to enjoy SnowflakeZ.\n',
    'What\'s your Favorite? Comment Below!\n',
    'Do you want to see more colors? Any other ideas? Comment Below!\n',
    'At the low floor price of 42 MATIC, how could you pass it up?\n',
    'A Snowflake for your thoughts?\n',
    'I WANT YOU!.... to buy a Snowflake :p \n',
    'Make sure to check out the sister collection #RainbowSnowflakeZNFT !\n',
    'Do you wanna build a snowman? No?.... What if it were made of SnowflakeZ? :p\n',
    'A lot of people talk about Special SnowflakeZ these days, were they referring to these?\n',
    'With a name like \'Queen\', you\'d think I\'d have more Followers :p\n',
    'You know what\'s funny? I HATE the cold!\n',
    'ERROR 404: Joke not found\n',
    'Real Snowflakes would be a lot better with more colours\n',
    'It\'s time to shill! At least it\'s my own project :p\n',
    'Twitter is pretty cool these days, but it\'d be cooler with SnowflakeZ!\n',
    'I may not have a checkmark, but look at my art!\n',
    'GIF me a break, GIF me a break, break me off a piece of that Broken Snowflake!\n',
    '5 SnowflakeZ in every set, don\'t let Twitter\'s link system fool you\n',
    'Broken Things are beautiful, too...\n',
    'They may be broken, but they have heart!\n',
    '@0xPolygon has always had my heart, only they could house my Broken Ones\n',
    'A Tribute to an Old Friend, these SnowflakeZ warm my heart\n',
]

links = [
    '22176117569172953848175605113995043088088791683134261308094269140051219709953',
    '22176117569172953848175605113995043088088791683134261308094269138951708082177',
    '22176117569172953848175605113995043088088791683134261308094269137852196454401',
    '22176117569172953848175605113995043088088791683134261308094269136752684826625',
    '22176117569172953848175605113995043088088791683134261308094269144449266221057',
    '22176117569172953848175605113995043088088791683134261308094269143349754593281',
    '22176117569172953848175605113995043088088791683134261308094269142250242965505',
    '22176117569172953848175605113995043088088791683134261308094269141150731337729',
    '22176117569172953848175605113995043088088791683134261308094269145548777848833',
    '22176117569172953848175605113995043088088791683134261308094269148847312732161',
    '22176117569172953848175605113995043088088791683134261308094269149946824359937',
    '22176117569172953848175605113995043088088791683134261308094269151046335987713',
    '22176117569172953848175605113995043088088791683134261308094269152145847615489',
    '22176117569172953848175605113995043088088791683134261308094269153245359243265',
    '22176117569172953848175605113995043088088791683134261308094269154344870871041',
    '22176117569172953848175605113995043088088791683134261308094269155444382498817',
    '22176117569172953848175605113995043088088791683134261308094269156543894126593',
    '22176117569172953848175605113995043088088791683134261308094269157643405754369',
    '22176117569172953848175605113995043088088791683134261308094269158742917382145',
    '22176117569172953848175605113995043088088791683134261308094269159842429009921',
    '22176117569172953848175605113995043088088791683134261308094269160941940637697',
    '22176117569172953848175605113995043088088791683134261308094269162041452265473',
    '22176117569172953848175605113995043088088791683134261308094269163140963893249',
    '22176117569172953848175605113995043088088791683134261308094269164240475521025',
    '22176117569172953848175605113995043088088791683134261308094269165339987148801',
    '22176117569172953848175605113995043088088791683134261308094269166439498776577',
    '22176117569172953848175605113995043088088791683134261308094269167539010404353',
    '22176117569172953848175605113995043088088791683134261308094269168638522032129',
    '22176117569172953848175605113995043088088791683134261308094269169738033659905',
    '22176117569172953848175605113995043088088791683134261308094269170837545287681',
    '22176117569172953848175605113995043088088791683134261308094269171937056915457',
    '22176117569172953848175605113995043088088791683134261308094269173036568543233',
    '22176117569172953848175605113995043088088791683134261308094269174136080171009',
    '22176117569172953848175605113995043088088791683134261308094269175235591798785',
    '22176117569172953848175605113995043088088791683134261308094269176335103426561',
    '22176117569172953848175605113995043088088791683134261308094269177434615054337',
    '22176117569172953848175605113995043088088791683134261308094269178534126682113',
    '22176117569172953848175605113995043088088791683134261308094269179633638309889',
    '22176117569172953848175605113995043088088791683134261308094269180733149937665',
]

hashtags_mentions = "#BrokenSnowflakeZNFT #NFT\n#NFTCommunity #NFTProject"

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Be sure to add replace the text of the with the text you wish to Tweet. You can also add parameters to post polls, quote Tweets, Tweet with reply settings, and Tweet to Super Followers in addition to other features.
# payload = {
#     "text": "Hashtag and link Test\nhttps://queen-linux-nfts.github.io/\n#RainbowSnowflakeZNFT"
# }
def sendTweet():
    payload = {
        "text": random.choice(greetings) + 'https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/' + random.choice(links) + "\n" + hashtags_mentions
    }



    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    # print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    print('\n'+json_response['data']['text'])

if __name__ == '__main__':
    for i in range(30):
        sendTweet()
        # timing = random.randint(180,300)
        print('Tweet # '+str(i+1))
        # print('Seconds to next: '+str(timing))
        # time.sleep(timing)
        time.sleep(300)