#!/usr/bin/node
const Rectangle = require('./4-rectangle').Rectangle;

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
