from curses import echo
from sqlite3 import connect
from sqlalchemy import *
import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker
from backend.database_access import DATABASE
from backend.db_interface import DatabaseInterface
from backend.classes import *

HOSTNAME = "vps.zgrate.ovh"
PORT = "3306"
USERNAME = "polrentex"
PASSWORD = "rentex123"
DB_NAME = "Rentex"

engine = sqlalchemy.create_engine('mysql://' + USERNAME + ':' + PASSWORD + '@' + HOSTNAME + ':' + PORT + '/' + DB_NAME)

class SQLAlchemyInterface(DatabaseInterface):
    
    def __init__(self):
        super().__init__()
        self.startSession: sqlalchemy.orm.sessionmaker = sessionmaker()
        engine.connect()
        self.startSession(bind=engine)

    def createSession(self) -> Session:
        return self.startSession()

    def authUser(self, login, password):
        pass

    def registerUser(
            self,
            name: str,
            surname: str,
            login: str,
            password: str,
            address: str,
            email: str,
            pesel: str,
    ):
        pass

    def getAccountStatus(self, userId: str):
        user = self.getUser(userId)
        if user is None:
            return None
        return user.status

    def getActivationToken(self, userId: str):
        user = self.getUser(userId)
        if user is None:
            return None
        return user.activationCode

    def setAccountStatus(self, userId: str, status: str):

        with self.createSession() as session:
            session.query(Client).filter(Client.id == userId).update({Client.status: status})
        pass

    def getUser(self, userId):
        with self.createSession() as session:
            return session.query(Client).get(userId)
        pass

    def setActivationToken(self, userId: int, token: str) -> bool:
        pass

    def changePassword(self, userId, newPwd):
        pass

    def updateLocation(self, carId, location):
        pass

    def rentalHistory(self, userId, pageIndex, pageLength):
        pass

    def getCards(self, userId):
        pass

    def addCard(self, userId, card: CreditCard):
        pass

    def browseNearestCars(self, location, distance):
        pass

    def browseNearestLocations(self, location, distance):
        pass

    def startReservation(self, reservation: Reservation):
        pass

    def startRental(self, userId, carId):
        pass

    def getRental(self, userId, rentalId):
        pass

    def endRental(self, rent: Rental):
        pass

    def getCars(self, pageIndex, pageCount, location, distance):
        pass

    def deleteCar(self, carId):
        pass

    def patchCar(self, carId, changes: dict):
        pass

    def getUsers(self, pageIndex, pageCount, filter: str):
        pass

    def deleteUser(self, userId):
        pass

    def patchUser(self, userId, changes: dict):
        pass

    def getCard(self, userId, cardId):
        pass

    def addLocation(self, location: Location):
        pass

    def getLocations(self, pageIndex, pageCount, location, distance):
        pass

    def deleteLocation(self, locationId):
        pass

    def patchLocation(self, locationId, changes: dict):
        pass

    def serviceCar(self, carId, userId, locationId, description="") -> str:
        pass

    def endService(self, service: Service):
        pass

    def getService(self, serviceId):
        pass

    def getServicesHistory(self, carId):
        pass

    def setNewBalance(self, user_id, new_balance) -> bool:
        pass

    def getBalance(self, user_id) -> str:
        pass

    def isUserWithEmailInDB(self, email) -> bool:
        pass

    def isUserWithLoginInDB(self, login) -> bool:
        pass

    def addCar(self, car: 'dict'):
        pass


    def dropCars(self):
        pass

    def dropRentalArchive(self):
        pass

    def dropUsers(self):
        pass

    def dropLocations(self):
        pass

    def userCleanup(self, user_id):
        pass

    def carCleanup(self, car_id):
        pass
