from neo4j import GraphDatabase
import os

class Neo4jLoader:
    def __init__(self, uri, user, password):
        """
        Initialize the Neo4j driver.
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        """
        Close the Neo4j driver connection.
        """
        if self.driver:
            self.driver.close()

    def load_users(self, file_path):
        """
        Load users into the Neo4j database from a CSV file.
        """
        query = """
        LOAD CSV WITH HEADERS FROM $file_path AS row
        CREATE (:User {userId: row.userId});
        """
        with self.driver.session() as session:
            session.run(query, file_path=f"file://{file_path}")

    def load_tweets(self, file_path):
        """
        Load tweets into the Neo4j database from a CSV file.
        """
        query = """
        LOAD CSV WITH HEADERS FROM $file_path AS row
        CREATE (:Tweet {tweetId: row.tweetId, content: row.content});
        """
        with self.driver.session() as session:
            session.run(query, file_path=f"file://{file_path}")

    def load_hashtags(self, file_path):
        """
        Load hashtags into the Neo4j database from a CSV file.
        """
        query = """
        LOAD CSV WITH HEADERS FROM $file_path AS row
        CREATE (:Hashtag {hashtagId: row.hashtagId, name: row.name});
        """
        with self.driver.session() as session:
            session.run(query, file_path=f"file://{file_path}")

if __name__ == "__main__":
    # Neo4j credentials
    URI = "bolt://localhost:7687"
    USER = "neo4j"
    PASSWORD = "password"

    # File paths (ensure these are uploaded to Neo4j's import directory)
    USERS_CSV = "users.csv"
    TWEETS_CSV = "tweets.csv"
    HASHTAGS_CSV = "hashtags.csv"

    # Verify files exist
    for file in [USERS_CSV, TWEETS_CSV, HASHTAGS_CSV]:
        if not os.path.exists(file):
            raise FileNotFoundError(f"File not found: {file}")

    # Load data into Neo4j
    loader = Neo4jLoader(URI, USER, PASSWORD)

    try:
        print("Loading users...")
        loader.load_users(USERS_CSV)

        print("Loading tweets...")
        loader.load_tweets(TWEETS_CSV)

        print("Loading hashtags...")
        loader.load_hashtags(HASHTAGS_CSV)

        print("Data successfully loaded into Neo4j.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        loader.close()
