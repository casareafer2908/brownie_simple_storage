// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    // Declare an int to save a number
    uint256 favoriteNumber;

    // create a class People with 2 parameters
    struct People {
        uint256 favoriteNumber;
        string name;
    }
    // Create an array of People
    People[] public people;
    // creates a mapping of a string to an int - a mapping is a reference
    mapping(string => uint256) public nameToFavoriteNumber;

    // saves a number
    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    // Reads a number
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    //adds a person(name and favorite number) to the array
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        //adds the mapping structure to the person array, so when you search a name
        //you get the favorite number back
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
