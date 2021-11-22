from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if not re.search("^[a-z]+$",username):
            raise UserInputError("Username must contain only letters")
        
        if not len(username)>2:
            raise UserInputError("Username must be at least 3 characters long")
        
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already in use")

        if not re.search("[^a-z]",password):
            raise UserInputError("Password cannot contain only letters")

        if not len(password)>7:
            raise UserInputError("Password must at least 8 characters long")




        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
