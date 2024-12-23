import os
import boa
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account
from dotenv import load_dotenv

load_dotenv()

MY_CONTRACT = "0x5FbDB2315678afecb367f032d93F642f64180aa3"
# Address
# ABI

def main():
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)

    # @dev Compile the contract and get ABI with load_partial
    favorites_deployer = boa.load_partial("favorites.vy")
    favorites_contract = favorites_deployer.at(MY_CONTRACT)

    print(f"Favorite number is {favorites_contract.retrieve()}")

    favorites_contract.store(777)
    print(f"Favorite number updated is {favorites_contract.retrieve()}")

if __name__ == "__main__":
    main()