from jose import jwt 
from datetime import datetime, timedelta
import os 
from dotenv import load_dotenv


# SECRET_KEY="S#e#c#r#e#t"#os.load_dotenv()
# ALGORITHM="HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES=60
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)
