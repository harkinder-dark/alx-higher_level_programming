#!/usr/bin/node
class Rectangle {
  constructor (h, w) {
    if (typeof(h) === 'number' && typeof(w) === 'number' && h === 0 && w === 0) {
      this.width = w;
      this.height = h;
    }  
  }

  print () {
    let m = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) m += 'X';
      console.log(m);
    }       
  }
}