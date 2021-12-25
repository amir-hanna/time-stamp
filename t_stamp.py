from tinydb import TinyDB, Query
import time
import os



def GetAbsScriptPath():
    AbsScriptPath = os.path.abspath( __file__ )
    AbsScriptPath_no_extension = AbsScriptPath.rpartition('.')[0]
    if not AbsScriptPath_no_extension:
        AbsScriptPath_no_extension = AbsScriptPath
    return (AbsScriptPath, AbsScriptPath_no_extension)
    
def get_db():
    strDatabasePath = GetAbsScriptPath()[1] + '.json'
    db = TinyDB(strDatabasePath)
    return db

        
def get_ts():
    with get_db() as db:
        q = Query()
        lst_result = db.search(q.stamp >= 0)

        if len(lst_result) == 0:
            return 0
        
        return lst_result[0]['stamp']
    

def write_ts():
    ts = time.time()
    with get_db() as db:
        q = Query()
        # update stamp if it exists otherwise insert it
        db.upsert({'stamp': ts}, q.stamp >= 0)


def too_recent(span_seconds):
    if time.time() >= get_ts() + span_seconds:
        return False
    return True
    
