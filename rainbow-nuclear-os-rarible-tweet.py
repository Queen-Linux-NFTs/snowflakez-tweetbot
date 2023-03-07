from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import os
import random
import time

load_dotenv()

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")

greetings = [
    'Plenty of SnowflakeZ for the picking!\n',
    'Find a unique Snowflake for a unique person\n',
    'Real Snowflakes aren\'t unique, but these SnowflakeZ are!\n',
    'It doesn\'t need to be the holidays to enjoy SnowflakeZ.\n',
    'What\'s your Favorite? Comment Below!\n',
    'A Snowflake for your thoughts?\n',
    'I WANT YOU!.... to buy a Snowflake :p \n',
    'Do you wanna build a snowman? No?.... What if it were made of SnowflakeZ? :p\n',
    'A lot of people talk about Special SnowflakeZ these days, were they referring to these?\n',
    'With a name like \'Queen\', you\'d think I\'d have more Followers :p\n',
    'You know what\'s funny? I HATE the cold!\n',
    'ERROR 404: Joke not found\n',
    'Real Snowflakes would be a lot better with more colours\n',
    'It\'s time to shill! At least it\'s my own project :p\n',
    'Twitter is pretty cool these days, but it\'d be cooler with SnowflakeZ!\n',
    'I may not have a checkmark, but look at my art!\n',
    'There\'s No FlakeZ like SnowflakeZ!\n',
    'You must buy, You must buy, You must buuuuuy.... SnowflakeZ\n',
    'SnowflakeZ keep falling on my head... Wait, it\'s supposed to be raindrops? Nah :p\n',
    'Shoutout to @opensea and @rarible for making great platforms for people to share and sell their #NFTs :)\n',
]

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


def sendTweet():
    hashtags_mentions = "#NFT #NFTArt\n#NFTProject"
    nuclear = ['https://opensea.io/assets/matic/0x40aff4cf882b28e748ea4bc9d20f587b76157482/','https://rarible.com/token/polygon/0x40aff4cf882b28e748ea4bc9d20f587b76157482:']
    rainbow = ['https://opensea.io/assets/matic/0x90253087c959b77f9b5b003a20cdac46a5e599a3/','https://rarible.com/token/polygon/0x90253087c959b77f9b5b003a20cdac46a5e599a3:']
    collection = random.choice((rainbow,nuclear))

    if collection == rainbow:
        hashtags_mentions+="\n#RainbowSnowflakeZNFT"
        tokenamount=1000
        greetings.extend([
            'At the low floor price of 10 MATIC, how could you pass it up?\n',
            'Make sure to check out the sister collection #NuclearSnowflakeZNFT !\n',
            ])

    if collection == nuclear:
        hashtags_mentions+="\n#NuclearSnowflakeZNFT"
        tokenamount=100
        greetings.extend([
            'At the low floor price of 5.5 MATIC, how could you pass it up?\n',
            'Make sure to check out the sister collection #RainbowSnowflakeZNFT !\n',
            ])
    
    payload = {
        "text": random.choice(greetings) + random.choice(collection) + str(random.randint(1,tokenamount)) + "\n" + hashtags_mentions
    }


    #Making the request
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
    tweets = 100
    for i in range(tweets):
        sendTweet()
        # timing = random.randint(180,300)
        print('Tweet #'+str(i+1)+' of '+str(tweets))
        # print('Seconds to next: '+str(timing))
        # time.sleep(timing)
        time.sleep(300)