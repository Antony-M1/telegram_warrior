# summary:

This documentation will help you setup the project locally

### Step 1:
Clone the project
```
git clone https://github.com/Antony-M1/telegram_warrior.git
```

### Step 2:
Create the environement using `python3.10+`
```
python -m venv env
```
Activate the `env`
```
source env/bin/activate
```

### Step 3:
Install all the requirements
```
pip install -r requirements.txt
```

### Step 4:
Start the project
The command `uvicorn main:app` refers to:

`main`: the file` main.py` (the Python "module").

`app`: the object created inside of `main.py` with the line `app = FastAPI()`.

`--reload`: make the server restart after code changes. Only do this for `development`.