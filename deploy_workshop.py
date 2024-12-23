import os
import boa
import getpass
from eth_account import Account
from boa.network import NetworkEnv, EthereumRPC
from dotenv import load_dotenv

load_dotenv()

def main():
    """
    Deploy vyper contract with boa for CU workshop
    @dev Test purpose only
    """
    print("Setting up boa env...")
    rpc = input("Enter RPC URL:\n")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    print("Setting up account...")
    private_key = getpass.getpass("Enter your private key: ")
    my_account = Account.from_key(private_key)
    boa.env.add_account(my_account, force_eoa=True)

    print("Deploying contract...")
    workshop_contract = boa.load("workshop.vy")

    print(f"Contract address is {workshop_contract.address}")

    previous_boolean = workshop_contract.get_bool()
    print(f"Previous boolean is {previous_boolean}")

    print("Updating boolean...")
    workshop_contract.set_bool(True)

    new_boolean = workshop_contract.get_bool()
    print(f"New boolean is {new_boolean}")

if __name__ == "__main__":
    main()