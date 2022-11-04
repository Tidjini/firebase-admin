'''Setup for setting up firebase admin setup'''

import firebase_admin
import utils
from .constants import CONFIG_FILE


class FirebaseAdmin:
    '''FirebaseAdmin

    Represent class that containe the global firebase database, 
    and we can use it over our application'''

    firebase_database = None

    @classmethod
    def setup(cls) -> None:
        try:
            file = utils.get_config_file(CONFIG_FILE)
            certification = firebase_admin.creadentials.Certificate(file)
            firebase_admin.initialize_app(certification)
            cls.firebase_database = firebase_admin.firestore_client()

        except FileExistsError as error:
            print(error)


# Setup this module in launch of your application
FirebaseAdmin.setup()
# Use this reference for your operations with firestore
database = FirebaseAdmin.firebase_database
