import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Settings():
    ENV=str(os.getenv("ENVIROMENT"))
    
    DATABASE_CONNECTION_STRING:str=os.getenv("LOCAL_DATABASE_CONNECTION_STRING",default="") if str(os.getenv("ENVIROMENT"))=="DEV"else os.getenv("DATABASE_CONNECTION_STRING",default="")
    
    SECRET_KEY: str =os.getenv("SECRET_KEY",default="")  
    ALGORITHM: str = "HS256"  # JWT algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Access token expiration time
    NO_REPLY_FROM_EMAIL=os.getenv("NO_REPLY_FROM_EMAIL",default="")
    SUPPORT_FROM_EMAIL=os.getenv("SUPPORT_FROM_EMAIL",default="")
    PASSWORD_RECOVER_EMAIL_EXPIRE_HOURS=3
    RESEND_API_KEY=os.environ["RESEND_API_KEY"]
    
    
    
