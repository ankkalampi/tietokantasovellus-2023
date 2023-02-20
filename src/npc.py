from user import get_user
from db import db
from sqlalchemy.sql import text





class NPC:
    def __init__(self, dialogue_list):
        self.dialogue_list = dialogue_list




def create_npc(name, username):
    user = get_user(username)
    user_id = user.id
    sql = text("INSERT INTO npcs(name, user_id) VALUES (:name, :user_id)")
    db.session.execute(sql, {"name":name, "user_id":user_id})
    db.session.commit()

def get_npcs(username):
    user = get_user(username)
    user_id = user.id
    sql = text("SELECT * FROM npcs WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    npcs = result.fetchall()
    return npcs