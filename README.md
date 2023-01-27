Prerequisites:
  1. rust installed
    --> if not, you want to get rustup
    
  2. python installed
    2a. matplotlib installed (probably a pip install matplotlib)
    
To run the code:

BE IN ROOT DIR

step 1 --> create python virtual enviroment
  python3 -m venv .env
  source .env/bin/activated
  
step 2 --> setup maturin
  pip install maturin
  maturin develop
  
step 3 --> run python script
  python3 scripts/sim.py
