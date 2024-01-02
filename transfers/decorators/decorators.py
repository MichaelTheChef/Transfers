import pymongo
import time
import uuid

# Connect

client = pymongo.MongoClient('mongodb+srv://michaaelexe:Stown0414@cluster0.kj7dphx.mongodb.net')
db = client.Molex

levels = ["molex", "transfers", "training", "system"]

def stopwatch(func):
    """Time a function"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed_time = end - start
        elapsed_time = round(elapsed_time)
        # Log the elapsed time to the database
        id = _log(f"Stopwatch: Time elapsed for {func.__name__} function: {elapsed_time} seconds", level="system")
        print(f"Stopwatch: Time elapsed: {elapsed_time} seconds, id: {id}")
        return result
    return wrapper

def debug(func):
    """Debug a function"""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            id = _log(f"Debug: {func.__name__} function ran successfully", level="system")
            print(f"Debug: {func.__name__} ran successfully, id: {id}")
            return result
        except Exception as e:
            id = _log(f"Debug: Exception occurred in {func.__name__} function: {e}", level="system")
            print(f"Debug: Exception occurred: {e}, id: {id}")
    return wrapper

def info(note: str, level: str = "molex"):
    """Take notes on a function"""
    def inner_func(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            id = _log(f"Note: Saved note, {note} on {func.__name__} function to {level} catalog. Result: {result}", level=level)
            print(f"Note: Saved note, {note} to {level} catalog, id: {id}, result: {result}")
            return result
        return wrapper
    return inner_func

def _log(message: str, level: str = "molex", id = uuid.uuid4()) -> uuid:
    """Log data to the database"""
    local_db = db
    local_collection = (local_db[f"{level}_logs"] if level in levels else local_db.system_logs)

    # The id can be likened to the session id or instance id
    local_collection.insert_one({"id": str(id), "message": message, "level": level})
    return id


