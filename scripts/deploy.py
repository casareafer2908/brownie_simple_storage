from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    # deploy
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)

    # save a number in the contract
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    # retrieve the saved number
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


# get the accound pre-configured in brownie, if the network is marked as development, it will use one of the
# accounts provided by the local blockchain (ie. ganache provides 10 funded accounts)
def get_account():
    if network.show_active() == "development":
        return accounts[0]
        # otherwise, it will ad an account from wallets (this one uses environemnt variables currently saved in .env)
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
