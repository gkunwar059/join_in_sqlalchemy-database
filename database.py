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
    
       
class Post(Base):
    __tablename__='posts'
    id=mapped_column(Integer,primary_key=True)
    title=mapped_column(String,nullable=True)
    user_id=mapped_column(Integer,ForeignKey('users.id'))
    user=relationship('User',back_populates='posts')
    
    

class Company(Base):
    __tablename__='companies'
    
    id=mapped_column(Integer,primary_key=True)
    name=mapped_column(String,nullable=False)
    
class Department(Base):
    __tablename__='departments'
    
    id=mapped_column(Integer,primary_key=True)
    name=mapped_column(String,nullable=False)
    company_id=mapped_column(Integer,ForeignKey('companies.id'))
    
class Employees(Base):
    __tablename__='employees'
    id=mapped_column(Integer,primary_key=True)
    name=mapped_column(String,nullable=True)
    salary=mapped_column(Integer,nullable=True)
    department_id=mapped_column(Integer,ForeignKey('departments.id'))
        
Base.metadata.create_all(engine)

# join ----company,department and employees   (( Joining 2 tables))
# results=session.query(Employee,Department).join(Department,Department.id==Employee.department_id).all()
# for employee, department in results:
#     print(employee.name,department.name)
    

#JOINING 3 tables 
result=session.query(Employees,Department,Company).select_from(Employees).join(Department).join(Company).filter(Company.name=='HydoPower').all()

for employe4,department,company in result:
    print(employe4.name,department.name,company.name)
    










# =======================================================================================================
# inner join of this table 
# inner_join=session.query(User,Post).join(User).first()
# print(inner_join)


# left outer join
# left_outer_join=session.query(User,Post).join(User).first()
# print(left_outer_join)

# outer join 
# outer_join=session.query(User,Post).outerjoin(User).first()
# print(outer_join)

# FULL(OUTER)JOIN:
# full_outer_join=session.query(User,Post).outerjoin(Post).union_all(session.query(User,Post).outerjoin(User)).all()
# print(full_outer_join)

# CROSS JOIN:

# cross_join=session.query(User,Post).all()
# print(cross_join)

