from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.utils.jwt_handler import create_access_token
import bcrypt

def register_user(db: Session, user_data: UserCreate):
    hashed_pw = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt())
    user = User(username=user_data.username, email=user_data.email, password=hashed_pw.decode('utf-8'))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "Usuario creado"}

def login_user(db: Session, login_data: UserLogin):
    user = db.query(User).filter(User.username == login_data.username).first()
    if not user or not bcrypt.checkpw(login_data.password.encode('utf-8'), user.password.encode('utf-8')):
        return {"error": "Credenciales inválidas"}
    token = create_access_token(data={"user_id": user.id, "username": user.username})
    return {"access_token": token}
