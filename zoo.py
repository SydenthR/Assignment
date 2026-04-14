# 11.1 - zoo.py
def hours():
    print("Open 9-5 daily")
import zoo
zoo.hours()

# 11.2 - Import with Alias

import zoo as menagerie
menagerie.hours()

# 16.8 - SQLAlchemy (books.db)

from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///books.db')
with engine.connect() as conn:
    result = conn.execute(text("SELECT title FROM book ORDER BY title ASC"))
    
    for row in result:
        print(row[0])