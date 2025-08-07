import sqlite3

# Connect to the database (replace with your database file path)

# The coach you're searching for
def query_collections (db_path, target_team):
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  # SQL query to find rows where the coach is either home or visitor
  query = """
  SELECT * FROM games
  WHERE home_coach = ? OR visitor_coach = ?
  """

  # Execute the query with parameters to prevent SQL injection
  cursor.execute(query, (target_team, target_team))

  # Fetch all matching rows
  results = cursor.fetchall()

  # Close the connection
  conn.close()

  return results
