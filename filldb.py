from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, MetaData,Column, String, Integer, Table
import sqlalchemy
from database_setup import engine
from models import Patente
from helpers import Helper

#book = session.query(Book).filter_by(Book.title == "The Stand").one_or_none()
pairing = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
class PatentePipeline:
    def __init__(self, db_engine=engine) -> None:
        self.engine = db_engine
        if not self.engine.dialect.has_table(self.engine, "patentes"):
            metadata = MetaData(self.engine)
            patentes = Table("patentes", metadata,
                Column('id', Integer, primary_key=True, autoincrement=True, nullable=False), 
                Column('patente', String))
            # Implement the creation
            metadata.create_all()

    def open_session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def close_session(self):
        self.session.close()

    def create_patent(self, patente):
        try:
            patente = Patente(patente = patente)
            self.session.add(patente)
            self.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e: print(f'{e.orig}')

    def get_patent(self,id):
        patent = (
            self.session.query(Patente)
            .filter_by(id=id)
            .first()
        )
        if patent is not None: 
            return patent.patente
        else:
            return "No se ha encontrado"

    def get_id(self, patente):
        patent = (
            self.session.query(Patente)
            .filter_by(patente=patente)
            .first()
        )
        if patent is not None: 
            return patent.id
        else:
            return "No se ha encontrado"

    def fulldb(self):
        total = (26**4)*(10**3)
        rows = self.session.query(Patente).count()
        if(rows == total):
            return "isFull"
        else:
            print("Start filling the db")
            helper = Helper()
            actual = "AAAA000"
            past = "noPast"
            for i in range(1,total+1):
                if past == "noPast":
                    past = actual
                    #actual = helper.createNewPatent(1,1,1,1,0) ERROR ENCONTRADO Y SOLUCIONADO
                    try:
                        patente = Patente(patente = actual)
                        self.session.add(patente)
                        self.session.commit()
                    except sqlalchemy.exc.SQLAlchemyError as e: print(f'{e.orig}')
                elif past != 'ZZZZ999':
                    number = int(actual[4::])
                    past = actual
                    actual = helper.createNewPatent(pairing[actual[0]],pairing[actual[1]],pairing[actual[2]],pairing[actual[3]],number)
                    try:
                        patente = Patente(patente = actual)
                        self.session.add(patente)
                        self.session.commit()
                    except sqlalchemy.exc.SQLAlchemyError as e: print(f'{e.orig}')
            rows = self.session.query(Patente).count()
            print("Finish the fill")
            return [rows,"Finish"]
    