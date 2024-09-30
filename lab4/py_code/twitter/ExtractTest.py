import pytest
from datetime import datetime
from Extract import Extract
from Tweet import Tweet
from Timespan import Timespan


def test_get_timespan():
    # Create sample tweets
    tweet1 = Tweet(1, "user1", "Hello world", datetime(2024, 1, 1, 10, 0, 0))
    tweet2 = Tweet(2, "user2", "Goodbye world", datetime(2024, 1, 2, 10, 0, 0))
    tweet3 = Tweet(3, "user3", "Hello again", datetime(2024, 1, 1, 12, 0, 0))
    
    # Test case 1: Minimum time span covering all tweets
    tweets = [tweet1, tweet2, tweet3]
    expected_timespan = Timespan(datetime(2024, 1, 1, 10, 0, 0), datetime(2024, 1, 2, 10, 0, 0))
    assert Extract.get_timespan(tweets) == expected_timespan

    # Test case 2: Single tweet
    tweet4 = Tweet(4, "user4", "Just one tweet", datetime(2024, 1, 1, 15, 0, 0))
    tweets = [tweet4]
    expected_timespan = Timespan(datetime(2024, 1, 1, 15, 0, 0), datetime(2024, 1, 1, 15, 0, 0))
    assert Extract.get_timespan(tweets) == expected_timespan

    # Test case 3: No tweets
    tweets = []
    with pytest.raises(ValueError):
        Extract.get_timespan(tweets)


def test_get_mentioned_users():
    # Create sample tweets
    tweet1 = Tweet(1, "user1", "Hello @user2 and @user3", datetime(2024, 1, 1, 10, 0, 0))
    tweet2 = Tweet(2, "user2", "Goodbye @user1", datetime(2024, 1, 2, 10, 0, 0))
    tweet3 = Tweet(3, "user3", "No mentions here", datetime(2024, 1, 1, 12, 0, 0))
    
    # Test case 1: Extracted mentioned users
    tweets = [tweet1, tweet2, tweet3]
    expected_users = {"user1", "user2", "user3"}
    assert Extract.get_mentioned_users(tweets) == expected_users

    # Test case 2: No mentions
    tweet4 = Tweet(4, "user4", "No mentions here", datetime(2024, 1, 1, 15, 0, 0))
    tweets = [tweet4]
    expected_users = set()
    assert Extract.get_mentioned_users(tweets) == expected_users

    # Test case 3: Duplicate mentions
    tweet5 = Tweet(5, "user5", "Mentioning @user2 again", datetime(2024, 1, 1, 16, 0, 0))
    tweets = [tweet1, tweet5]
    expected_users = {"user2", "user3"}
    assert Extract.get_mentioned_users(tweets) == expected_users

