import getpass
from dotenv import load_dotenv
import os
import uuid

load_dotenv()


def _set_if_undefined(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"Please provide your {var} in .env")


_set_if_undefined("OPENAI_API_KEY")