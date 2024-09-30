import pytest
from datetime import datetime
from Tweet import Tweet
from Timespan import Timespan
from Filter import Filter


def test_written_by():
    # Create sample tweets
    tweet1 = Tweet(1, "user1", "Hello world", datetime(2024, 1, 1, 10, 0, 0))
    tweet2 = Tweet(2, "user2", "Goodbye world", datetime(2024, 1, 2, 10, 0, 0))
    tweet3 = Tweet(3, "user1", "Another tweet", datetime(2024, 1, 3, 10, 0, 0))
    
    # Test case 1: Get all tweets written by user1
    tweets = [tweet1, tweet2, tweet3]
    filtered_tweets = Filter.written_by(tweets, "user1")
    assert filtered_tweets == [tweet1, tweet3]

    # Test case 2: Get all tweets written by user2
    filtered_tweets = Filter.written_by(tweets, "user2")
    assert filtered_tweets == [tweet2]

    # Test case 3: No tweets by user3
    filtered_tweets = Filter.written_by(tweets, "user3")
    assert filtered_tweets == []


def test_in_timespan():
    # Create sample tweets
    tweet1 = Tweet(1, "user1", "Hello world", datetime(2024, 1, 1, 10, 0, 0))
    tweet2 = Tweet(2, "user2", "Goodbye world", datetime(2024, 1, 2, 10, 0, 0))
    tweet3 = Tweet(3, "user3", "Another tweet", datetime(2024, 1, 3, 10, 0, 0))

    # Test case 1: Get tweets within a timespan
    timespan = Timespan(datetime(2024, 1, 1, 9, 0, 0), datetime(2024, 1, 2, 11, 0, 0))
    tweets = [tweet1, tweet2, tweet3]
    filtered_tweets = Filter.in_timespan(tweets, timespan)
    assert filtered_tweets == [tweet1, tweet2]

    # Test case 2: No tweets in the timespan
    timespan = Timespan(datetime(2025, 1, 1, 9, 0, 0), datetime(2025, 1, 1, 10, 0, 0))
    filtered_tweets = Filter.in_timespan(tweets, timespan)
    assert filtered_tweets == []

    # Test case 3: Exact match on a tweet's timestamp
    timespan = Timespan(datetime(2024, 1, 2, 10, 0, 0), datetime(2024, 1, 2, 10, 0, 0))
    filtered_tweets = Filter.in_timespan(tweets, timespan)
    assert filtered_tweets == [tweet2]


def test_containing():
    # Create sample tweets
    tweet1 = Tweet(1, "user1", "Hello world", datetime(2024, 1, 1, 10, 0, 0))
    tweet2 = Tweet(2, "user2", "Goodbye world", datetime(2024, 1, 2, 10, 0, 0))
    tweet3 = Tweet(3, "user3", "Another amazing tweet", datetime(2024, 1, 3, 10, 0, 0))

    # Test case 1: Tweets containing "world"
    words = ["world"]
    tweets = [tweet1, tweet2, tweet3]
    filtered_tweets = Filter.containing(tweets, words)
    assert filtered_tweets == [tweet1, tweet2]

    # Test case 2: Tweets containing "amazing"
    words = ["amazing"]
    filtered_tweets = Filter.containing(tweets, words)
    assert filtered_tweets == [tweet3]

    # Test case 3: No tweets containing "random"
    words = ["random"]
    filtered_tweets = Filter.containing(tweets, words)
    assert filtered_tweets == []

    # Test case 4: Case-insensitive search
    words = ["WORLD"]
    filtered_tweets = Filter.containing(tweets, words)
    assert filtered_tweets == [tweet1, tweet2]


# To run the tests, simply run: pytest FilterTest.py

