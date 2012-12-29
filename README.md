#Between The Tweets

Peter Swire - swirepe.com

##What is it?

It's a [twitter bot](https://twitter.com/Between_Tweets) that posts random sentences from literotica.com.  How fun!

Note: I don't own literotica.com, and I am not including their content with this script.  You can either build it all up yourself, or break the password on that archive.

##How does it work?

* wget to gather data
* nltk for sentence discovery
* python-twitter to post online
* amazon aws for the server

As a bonus feature, you can run `strfile` over the processed stories and have exciting `fortune`'s.  The delimiter is right for that and everything.

##Oh, Also

Special thanks fo [@snatiabir](https://twitter.com/snatiabir) for suggesting that particular unsupervised machine learning algorithm in the Natural Language Tool Kit.  It takes a special kind of friend to use her Ph.D. training on Christmas day to help me make a novelty twitter account.
