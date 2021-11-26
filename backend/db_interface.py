from models import *


# TODO: POPprzenosiłem


class DatabaseInterface:

    def authUser(self, login, password):
        """
        :param login:
        :param password:
        :return None if not authorized, user_id if authorized
        """
        pass

    def registerUser(self, name: str, surname: str, login: str, password: str, address: str, email: str, pesel: str):
        """
       :param name:
       :param surname:
       :param gender:
       :param login:
       :param password:
       :param address:
       :param email:
       :param pesel:
       :return None if any error, user_id if success
       """
        pass

    def registerUser(self, name: str, surname: str, gender: str, login: str, password: str, address: str, email: str,
                     pesel: str) -> str:
        """
        :param name:
        :param surname:
        :param gender:
        :param login:
        :param password:
        :param address:
        :param email:
        :param pesel:
        :return None if any error, user_id if success
        """
        pass

    def getUserToken(self, userId: str):
        pass

    def getAccountStatus(self, userId: str):
        """

        :param userId:
        :return Current status of the account as a str, or None if any error
        """
        pass

    def getActivationToken(self, userId: str):
        """

        :param userId:
        :return None if there is no token, or token of activation
        """
        pass

    def activateAccount(self, userId: str):
        """

        :param token:
        :return true if account activated, false if not
        """
        pass

    def getUser(self, userId) -> User:
        """

        :param userId:
        :return User, or None if any error
        """
        pass

    def setActivationToken(self, userId: int, token: str) -> bool:
        """

        :param userId:
        :param token: 6 digits pin
        :return true if successful, false if not

        """
        pass

    def changePassword(self, userId, newPwd):
        pass

    def updateLocation(self, userId, location: tuple[str, str]) -> bool:
        """
        :param userId:
        :param location: Tuple in form Latitude, Longitude
        :returns True if success false if not
        """
        pass  # TODO: useless?

    def rentalHistory(self, userId, pageIndex, pageLength):
        pass

    def getCards(self, userId):
        pass

    def addCard(self, userId, card: CreditCard) -> bool:
        """
        :param card Card object
        :returns True if succesfull, false if not
        """
        pass

    def deleteCard(self, userId, cardId):
        pass

    def browseNearestCars(self, location: tuple[str, str], distance) -> list["Car"]:
        """

        :param location: tuple, first location is Longitude, second is Latitude
        :param distance: this is already validated
        :returns list of cards. Can be empty. None if any error occured
        """
        pass

    def browseNearestLocations(
            self, location: tuple[str, str], distance
    ) -> list["Location"]:
        """

        :param location: tuple, first one is lat, second one is long
        :param distance:
        """
        pass

    def getCar(self, carId) -> Car:
        """

        :param carId:
        :return None if car not found, Car if found
        """
        pass

    def getLocation(self, locationId) -> Location:
        """

        :param locationId:
        :returns None if location not found, Location if found
        """
        pass

    def getReservation(self, userId, reservationId):
        pass

    def endReservation(self, reservation: Reservation) -> bool:
        """

        :param reservation: Reservation object, ready to stripped and put into DB
        :return True if success, false if not
        """
        pass

    def startReservation(self, reservation: Reservation) -> bool:
        """

        :param reservation: Reservation object, ready to stripped and put into DB
        :return True if success, false if not
        """
        pass

    def startRental(self, userId, rent: Rental) -> bool:
        """

        :param userId: User ID
        :param rent: Already calculated Rental. Only strip down Client_id
        :returns true if success, false if not
        """
        pass

    def getRental(self, userId, rentalId):
        pass

    def endRental(self, rent: Rental) -> bool:
        """

        :param rent: Already calculated and ready to be archived rental
        :returns True if success, False if not
        """
        pass

    def adminActive(self, userId):
        pass

    def acceptDocuments(self):
        pass

    def getCars(self, pageIndex, pageCount, location: tuple[str, str], distance):
        pass

    def addCar(self, car: 'Car'):
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

    def getUserRentalHistory(self, userId, pageIndex, pageLength) -> list[Rental]:
        """
        :param userId: id of user
        :param pageIndex: a page number
        :param pageLength: length of the page
        :returns List can be returned empty, if there is no Rental in this category
        """
        pass

    def addLocation(self, location: Location):
        pass

    def getLocations(self, pageIndex, pageCount, location: tuple[str, str], distance):
        pass

    def deleteLocation(self, locationId):
        pass

    def patchLocation(self, locationId, changes: dict):
        pass

    def serviceCar(self, carId):
        pass

    def endService(self, carId, serviceId):
        pass

    def getService(self, cardId, serviceId):
        pass

    def getServices(self, carId):
        pass

    def getCard(self, user_id, card_id) -> CreditCard:
        """

        :param user_id:
        :param card_id:
        :returns None if card not found or card is not a user card, CreditCard if it's okey
        """
        pass