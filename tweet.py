	# To fetch a single user's public status messages, where "user" is either
	# a Twitter "short name" or their user id.

	#   >>> statuses = api.GetUserTimeline(user)
	#   >>> print [s.text for s in statuses]

	# To use authentication, instantiate the twitter.Api class with a
	# consumer key and secret; and the oAuth key and secret:

	#   >>> api = twitter.Api(consumer_key='twitter consumer key',
	#                         consumer_secret='twitter consumer secret',
	#                         access_token_key='the_key_given',
	#                         access_token_secret='the_key_secret')

	#   >>> status = api.PostUpdate('I love python-twitter!')
	# >>> print status.text
	# I love python-twitter!

from chooseTweet import chooseLine
import logging
import sys
import twitter
import time

api = None


def setup():
    global api
    api = twitter.Api(consumer_key=open("consumer_key.txt").read().strip(),
        consumer_secret=open('consumer_secret.txt').read().strip(),
        access_token_key=open('access_token_key.txt').read().strip(),
        access_token_secret=open('access_token_secret.txt').read().strip())

		
def post(message):
    try:
        api.PostUpdate(message)
        logging.info("Posted message successfully!")
        return True
    except:
        logging.warn( "Failed to post message: %s" % message)
        return False


def main(retries=10):
    setup()

    posted = False
    for i in range(retries):
        msg = chooseLine("collected/")
        posted = post(msg)
        if posted:
            logging.info("Posted!")
            sys.exit(0)
        else:
            logging.warn("Failed to post, sleeping for 10 seconds.")
            time.sleep(10)
                
    logging.error("Too many retries; failing!")


if __name__ == "__main__":
    main()
