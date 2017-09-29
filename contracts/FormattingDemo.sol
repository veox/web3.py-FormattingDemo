pragma solidity ^0.4.0;

contract FormattingDemo {
    bytes public storageBytes;
    bytes20 public storageBytes20;
    address public storageAddress;
    string public storageString;

    function setBytes(bytes _arg) public returns(bytes) {
        storageBytes = _arg;
        return storageBytes;
    }
    function setBytes20(bytes20 _arg) public returns(bytes20) {
        storageBytes20 = _arg;
        return storageBytes20;
    }
    function setAddress(address _arg) public returns(address) {
        storageAddress = _arg;
        return storageAddress;
    }
    function setString(string _arg) public returns(string) {
        storageString = _arg;
        return storageString;
    }
}
