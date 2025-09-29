To run this project first create a virtual environment and activate it:

`python3 -m venv ../owloVenv`

`source ../owloVenv/bin/activate`

Then build the package

`pip install build`

`python -m build`

Install requirements
`pip install -e .`

Run the app
`python camera_profile_viewer/main.py`

For testing:
Install dev requirements
`pip install -e .[dev]`
`python -m pytest -vs`