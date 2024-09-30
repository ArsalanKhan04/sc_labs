from typing import List
from Tweet import Tweet
from Timespan import Timespan

class Filter:

    @staticmethod
    def written_by(tweets: List[Tweet], username: str) -> List[Tweet]:
        """
        Find tweets written by a particular user.
        
        Args:
            tweets: a list of Tweet objects with distinct ids.
            username: the username to filter tweets by (case-insensitive).
            
        Returns:
            A list of tweets written by the specified user, in the same order as in the input list.
        """
        return []
        return [tweet for tweet in tweets if tweet.author.lower() == username.lower()]

    @staticmethod
    def in_timespan(tweets: List[Tweet], timespan: Timespan) -> List[Tweet]:
        """
        Find tweets that were sent during a particular timespan.
        
        Args:
            tweets: a list of Tweet objects with distinct ids.
            timespan: a Timespan object representing the desired time interval.
            
        Returns:
            A list of tweets that were sent during the timespan, in the same order as in the input list.
        """
        return [tweet for tweet in tweets if timespan.start <= tweet.timestamp <= timespan.end]

    @staticmethod
    def containing(tweets: List[Tweet], words: List[str]) -> List[Tweet]:
        """
        Find tweets that contain certain words.
        
        Args:
            tweets: a list of Tweet objects with distinct ids.
            words: a list of words to search for in the tweets (case-insensitive).
            
        Returns:
            A list of tweets that contain at least one of the words, in the same order as in the input list.
        """
        words_lower = {word.lower() for word in words}
        return [tweet for tweet in tweets if any(word in tweet.text.lower().split() for word in words_lower)]

