from sqlalchemy import Integer,create_engine,String,ForeignKey,MetaData,select
from sqlalchemy.orm import Mapped,mapped_column,Session,sessionmaker,DeclarativeBase,relationship,MappedColumn,query,join,session

metadata=MetaData()

try:
    engine=create_engine('postgresql://postgres:123456789@127.0.0.1:5432/postgres',echo=False)
    print("Connection Sucessfully !")
except Exception as e:
    print(str(e))

with Session(engine) as session:
    Session=sessionmaker(bind=engine)
    session=Session()

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__='users'
    id:Mapped[int]=mapped_column(Integer,primary_key=True,nullable=False)
    name=mapped_column(String,nullable=False)
    phone_number=mapped_column(Integer,nullable=False)
    posts=relationship('Post',back_populates='user')
    comments=relationship('Comment',back_populates='user')
    
       
class Post(Base):
    __tablename__='posts'
    id=mapped_column(Integer,primary_key=True)
    title=mapped_column(String,nullable=True)
    user_id=mapped_column(Integer,ForeignKey('users.id'))
    user=relationship('User',back_populates='posts')
    
    
class Comment(Base):
    __tablename__='comments'
    id=mapped_column(Integer,primary_key=True)
    text=mapped_column(String,nullable=False)
    user_id=mapped_column(Integer,ForeignKey('users.id'))
    user=relationship('User',back_populates='comments')
    
Base.metadata.create_all(engine)

# new_user=session.query(User).join(Post).filter(Post.title=='ram').all()
# print(new_user)
    
    
statement=select(User).join(Post).filter(Post.title=='ram')

new_user=session.execute(statement).all()
print(new_user)


# query all the users
all_user=session.query(User).all()
print(all_user)
    

