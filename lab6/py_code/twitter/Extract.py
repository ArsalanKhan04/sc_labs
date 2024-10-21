from Timespan import Timespan
from Tweet import Tweet
from datetime import datetime
from typing import List, Set

class Extract:
    @staticmethod
    def get_timespan(tweets: List[Tweet]) -> Timespan:
        if not tweets:
            raise ValueError("The list of tweets cannot be empty.")

        # Get the minimum and maximum timestamps
        min_timestamp = min(tweet.timestamp for tweet in tweets)
        max_timestamp = max(tweet.timestamp for tweet in tweets)

        # Return a Timespan object
        return Timespan(min_timestamp, max_timestamp)

    @staticmethod
    def get_mentioned_users(tweets: List[Tweet]) -> Set[str]:
        mentioned_users = set()
        for tweet in tweets:
            text = tweet.text
            # Find all mentions in the tweet text
            words = text.split()
            for word in words:
                if word.startswith('@') and len(word) > 1:
                    username = word[1:]  # Remove the '@' symbol
                    if username.isalnum() or '_' in username or '-' in username:
                        mentioned_users.add(username.lower())  # Add in lowercase for case insensitivity

        return mentioned_users
