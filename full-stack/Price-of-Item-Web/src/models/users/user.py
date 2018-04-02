import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id = None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @staticmethod
    def is_valid_login(email, password):
        """
        This method verifies that an e-mail/password combo (sent from the website) is valid or not
        Checks that the email exists and the password specified is correct
        :param email: The User's e-mail
        :param password: A sha512 hashed password
        :return: True if valid, else False
        """

        user_data = Database.find_one(collection="users",
                                      query={"email": email}
                                      )
        if user_data is None:
            raise UserErrors.UserNotExistError("Your User does not Exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("Your Password is incorrect")

        return True