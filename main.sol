pragma solidity ^0.4.13;

contract MyToken {
  string public name;
  string public symbol;
  uint8 public decimals;
  uint256 public totalSupply;

  mapping (address => uint256) public balanceOf;

  event Transfer(address indexed from, 
    address indexed to, uint256 value);

  function MyToken(uint256 initialSupply, 
    string tokenName, uint8 decimalUnits, 
    string tokenSymbol) {
    balanceOf[msg.sender] = initialSupply;
    totalSupply = initialSupply;
    name = tokenName;
    symbol = tokenSymbol;
    decimals = decimalUnits;
  }

  function transfer(address _to, uint256 _value) {
    require(balanceOf[msg.sender] >= _value);
    require(balanceOf[_to] + _value > balanceOf[_to]);
    balanceOf[msg.sender] -= _value;
    balanceOf[_to] += _value;
    Transfer(msg.sender, _to, _value);
  }
}