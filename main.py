import itertools

from utils.database_startup import database_startup
from utils.db_queries import query_collections
from utils.create_ICalendar import create_ICalendar

from data.targetTeams import lolP,strkEl,wingIk

needDB = False

def main():


  print("Hello from scripts-csvtoicalendar!")
  if needDB:
    database_startup('./data/2025soccer.csv')

  # query coaches
  kiddo_striker = [row +(strkEl.kiddo,) for row in query_collections(db_path="./data/games.db",target_team=strkEl.team_name)]
  kiddo_wing =  [row +(wingIk.kiddo,) for row in query_collections(db_path="./data/games.db",target_team=wingIk.team_name)]
  kiddo_lollipop =  [row +(lolP.kiddo,) for row in query_collections(db_path="./data/games.db",target_team=lolP.team_name)]

  collecting_games = itertools.chain(kiddo_striker,kiddo_wing,kiddo_lollipop)
  print(len(list(collecting_games)))
  create_ICalendar(kiddo_striker + kiddo_wing + kiddo_lollipop)

if __name__ == "__main__":
    main()
