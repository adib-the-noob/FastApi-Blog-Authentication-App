from pydantic import BaseModel,EmailStr
from typing import List, Optional

class UserRegistrationSchema(BaseModel):
    email: EmailStr
    password: str
    password1: str

    class Config:
        schema_extra = {
            "example": {
                "email": "bigdeli.ali3@gmail.com",
                "password": "yourpassword",
                "password1": "yourpassword"
            }
        }

class ResponseUserRegistrationSchema(BaseModel):
    detail:str
    
    class Config:
        schema_extra = {
            "example": {
                "detail": "message content"
            }
        }
        
class UserLoginSchema(BaseModel):
    email: EmailStr 
    password: str 

    class Config:
        schema_extra = {
            "example": {
                "email": "bigdeli.ali3@gmail.com",
                "password": "yourpassword"
            }
        }
class ResponseUserLoginSchema(BaseModel):
    access_token: str 
    refresh_token: str 
    user_id: int
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "access_token": "accesstoken",
                "refresh_token": "refreshtoken",
                "email":"bigdeli.ali3@gmail.com",
                "user_id":1
                
            }
        }
class RefreshTokenSchema(BaseModel):
    refresh_token: str 

    class Config:
        schema_extra = {
            "example": {
                "refresh_token": "refreshtoken",                
            }
        }
class ResponseRefreshTokenSchema(BaseModel):
    refresh_token: str 
    access_token: str 
    class Config:
        schema_extra = {
            "example": {
                "access_token": "accesstoken",
                "refresh_token": "refreshtoken",                
            }
        }