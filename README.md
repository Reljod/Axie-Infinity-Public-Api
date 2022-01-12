
<img src="./images/api-logo.png" style=" float:left ; width:100px ">

# Axie-Infinity-Public-Api

Axie Infinity Public API built in Python Fast API.

<a href="https://marketplace.axieinfinity.com/axie/114259/">
    <img src="./images/my-axie.png" width="200">
</a>

## Usage

For local usage, the host is set to run in http://localhost:8000/. Running this
will route you to the ReDoc API Documentation.

To get all cards:
```
curl -H "Content-Type: application/json" -X POST http://localhost:8000/cards
```

## Developer Setup.
1. Clone the [repository](https://github.com/Reljod/Axie-Infinity-Public-Api).
    * `git clone git@github.com:Reljod/Axie-Infinity-Public-Api.git`
2. Install Python 3.10.0 in your local directory. Test it by running `python --version`.<br>
*Note that the code might not work if it's not*
*version 3.10.0 due to the usage of | for type hints.*
*Use typing.Union if we're using Python 3.9 or below.*
3. Under the root folder, *Axie-Infinity-Public-Api*, create a Python virtual environment named **.venv**.
    * `python -m venv .venv`
    * To activate virtual environment:
        * For windows: `.venv/Scripts/Activate.ps1`
        * For linux/mac: `source .venv/bin/activate`
4. Under the virtual environment, install necessary python packages.
    * `pip install -r requirements.txt`
5. After the setup, start the app by running the command: `uvicorn main:app --reload`. This should start the host
http://localhost:8000/. ***See Usage to see how to use the API***.
6. For testing, just execute the command: `pytest -v`