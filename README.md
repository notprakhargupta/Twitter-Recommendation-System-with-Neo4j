# Twitter Recommendation System

This project demonstrates how to build a recommendation system for tweets, hashtags, and users using Neo4j. The project uses interaction data to recommend tweets, hashtags, or users based on user activity and relationships.

## Project Overview

- **Database**: Neo4j
- **Language**: Python
- **Use Cases**:
  1. Recommend tweets based on user interactions (e.g., likes, retweets).
  2. Suggest hashtags based on the content of tweets and user behavior.
  3. Recommend users to follow based on mutual connections or shared interests.

## Dataset Information

This project is based on the **RecSys Challenge Dataset**. Due to the **copyrighted nature of the dataset**, the actual data files are not included in this repository. To replicate the system:
1. Download the dataset directly from the [RecSys Challenge website](https://www.recsyschallenge.com/).
2. Follow the dataset usage policies provided by RecSys.

To demonstrate the project, we have included a **sample dataset** (`users.csv`, `tweets.csv`, `hashtags.csv`) that mimics the structure of the original dataset. You can replace these files with the real dataset after downloading it.

## Files in the Repository

1. **`data/`**:
   - `users.csv`: Sample user data with `userId`.
   - `tweets.csv`: Sample tweet data with `tweetId` and `content`.
   - `hashtags.csv`: Sample hashtag data with `hashtagId` and `name`.

2. **`scripts/`**:
   - `load_data.py`: Python script to load the data into the Neo4j database.

3. **`README.md`**:
   - This file, providing an overview of the project and instructions.

## Steps to Run the Project

1. **Install Neo4j**:
   - Download and install Neo4j from [here](https://neo4j.com/download/).
   - Start the Neo4j server (default URL: `http://localhost:7474`).

2. **Prepare the Dataset**:
   - Place the sample dataset (`users.csv`, `tweets.csv`, `hashtags.csv`) in the Neo4j `import` directory. If using the original RecSys data, preprocess it to match the sample data structure.

3. **Run the Loader Script**:
   - Install Python dependencies:
     ```bash
     pip install neo4j
     ```
   - Update the `load_data.py` script with your Neo4j credentials:
     ```python
     loader = Neo4jLoader("bolt://localhost:7687", "neo4j", "your_password")
     ```
   - Run the script:
     ```bash
     python scripts/load_data.py
     ```

4. **Query the Database**:
   - Use Neo4j Browser or Cypher queries to test the recommendation system. Example queries are provided in the script.

## Recommendations

- **Tweets**:
  ```cypher
  MATCH (u:User)-[:LIKED]->(t:Tweet)<-[:LIKED]-(other:User)-[:LIKED]->(recommend:Tweet)
  WHERE u.userId = "1"
  RETURN recommend, COUNT(recommend) AS popularity
  ORDER BY popularity DESC
  LIMIT 10;
