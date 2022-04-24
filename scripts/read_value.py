from brownie import SimpleStorage, accounts, config

# when we do brownie compile, brownie reads all contracts from the contracts directory then "holds"
# it as an array, SimpleStorage Array will contain all the deployments done


def read_contract():
    # it takes the lenght of the array then does -1 to get the latest contract deployment
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
