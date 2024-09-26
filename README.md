# Steps to execute:
1. git clone https://github.com/MohammedAhmeduddin/ImprovedCalaculator
2. cd ImprovedCalaculator
3. python -m venv venv
4. source venv/bin/activate
5. pip install requirements.txt
# Command for testing:
1. pytest
2. pytest --cov=calculator --cov-report=term-missing
3. pytest --cov=calculator --cov-report=html
4. pylint calculator.py calculation.py history.py
